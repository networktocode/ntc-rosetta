from ntc_rosetta.translators.openconfig.ios.openconfig_interfaces.interfaces import (
    Interfaces,
)
from ntc_rosetta.translators.openconfig.ios.openconfig_network_instance.network_instances import (
    NetworkInstances,
)

from yangify import translator
from yangify.translator.config_tree import ConfigTree


class IOSTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result

        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    interfaces = Interfaces
    network_instances = NetworkInstances
