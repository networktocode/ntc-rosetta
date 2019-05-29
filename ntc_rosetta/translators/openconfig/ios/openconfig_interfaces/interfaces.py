from typing import Any, Dict, Optional

from ntc_rosetta.helpers import json_helpers as jh
from ntc_rosetta.translators.openconfig.ios.openconfig_if_ethernet import ethernet

from yangify.translator import Translator, TranslatorData, unneeded


class SubinterfaceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config"

    index = unneeded

    def description(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   description {value}")
        else:
            self.yy.result.add_command(f"   no description")


class Subinterface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"

        def pre_process_list(self) -> None:
            parent_key = self.keys["/openconfig-interfaces:interfaces/interface"]
            for element in self.to_remove:
                iface_name = f"{parent_key}.{element['index']}"
                self.root_result.add_command(f"no interface {iface_name}")

        def pre_process(self) -> None:
            parent_key = self.keys["/openconfig-interfaces:interfaces/interface"]
            self.keys["subinterface_key"] = f"{parent_key}.{self.key}"
            path = f"interface {self.keys['subinterface_key']}"
            if self.replace:
                self.root_result.add_command(
                    f"no interface {self.keys['subinterface_key']}"
                )
            self.result = self.root_result.new_section(path)

        def post_process(self) -> None:
            path = f"interface {self.keys['subinterface_key']}"
            if not self.result:
                self.root_result.pop_section(path)
            else:
                self.result.add_command("   exit\n!")

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

    def description(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   description {value}")
        else:
            self.yy.result.add_command(f"   no description")

    def enabled(self, value: Optional[bool]) -> None:
        if value:
            self.yy.result.add_command(f"   no shutdown")
        else:
            self.yy.result.add_command(f"   shutdown")


class Interface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface"

        def _remove_subinterfaces(self, interface: Dict[str, Any]) -> None:
            subifaces = jh.query("subinterfaces.subinterface[]", interface) or []
            for subiface in subifaces:
                self.root_result.add_command(
                    f"no interface {self.key}.{subiface['index']}"
                )

        def pre_process_list(self) -> None:
            for element in self.to_remove:
                self.result.add_command(f"default interface {element['name']}")
                self._remove_subinterfaces(element)

        def pre_process(self) -> None:
            if self.replace:
                self.root_result.add_command(f"default interface {self.key}")
                if self.running is not None:
                    self._remove_subinterfaces(self.running.goto(self.path).value)
            path = f"interface {self.key}"
            self.result = self.root_result.new_section(path)

        def post_process(self) -> None:
            path = f"interface {self.key}"
            if not self.result:
                self.root_result.pop_section(path)
            else:
                self.result.add_command("   exit\n!")

    name = unneeded

    subinterfaces = Subinterfaces
    config = InterfaceConfig
    ethernet = ethernet.Ethernet


class Interfaces(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces"

        def pre_process(self) -> None:
            pass

    interface = Interface
