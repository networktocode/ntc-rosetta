from ntc_rosetta.translators.openconfig.junos.openconfig_interfaces import interfaces
from ntc_rosetta.translators.openconfig.junos.openconfig_network_instance import (
    network_instances,
)

from lxml import etree

from yangify import translator


class JunosTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = etree.Element("configuration")
            self.result = self.root_result

        def post(self) -> None:
            self.root_result = etree.tostring(
                self.root_result, pretty_print=True
            ).decode()

    interfaces = interfaces.Interfaces
    network_instances = network_instances.NetworkInstances
