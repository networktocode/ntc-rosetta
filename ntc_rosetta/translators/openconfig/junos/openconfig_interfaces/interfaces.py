from typing import Optional

from lxml import etree

from ntc_rosetta.helpers import xml_helpers as xh
from ntc_rosetta.helpers.junos import delete_attr
from ntc_rosetta.translators.openconfig.junos.openconfig_if_ethernet import ethernet

from yangify.translator import Translator, TranslatorData, unneeded


class SubinterfaceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config"

    index = unneeded

    def description(self, value: Optional[str]) -> None:
        if value:
            etree.SubElement(self.yy.result, "description").text = value
        else:
            etree.SubElement(self.yy.result, "description", delete_attr())


class Subinterface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    unit = etree.SubElement(self.result, "unit", delete_attr())
                    etree.SubElement(unit, "name").text = str(element.value["index"])

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "unit")
            etree.SubElement(self.result, "name").text = str(self.key)

    index = unneeded

    config = SubinterfaceConfig


class Subinterfaces(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces"

    subinterface = Subinterface


class InterfaceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/config"

    name = unneeded
    type = unneeded
    description = unneeded  # not supported on parent config

    def enabled(self, value: Optional[bool]) -> None:
        if value:
            etree.SubElement(self.yy.result, "disable", delete_attr())
        else:
            etree.SubElement(self.yy.result, "disable")


class Interface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    xpath = f"interface[name={element.value['name']}]"
                    xh.find_or_create(self.root_result, xpath, delete_attr())

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "interface")
            etree.SubElement(self.result, "name").text = self.key

    name = unneeded

    subinterfaces = Subinterfaces
    config = InterfaceConfig
    ethernet = ethernet.Ethernet


class Interfaces(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.root_result, "interfaces")
            if self.replace:
                self.result.attrib["replace"] = "replace"

    interface = Interface
