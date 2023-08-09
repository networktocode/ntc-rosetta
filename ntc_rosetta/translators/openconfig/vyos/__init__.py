from ntc_rosetta.helpers.request_list import RequestList
from ntc_rosetta.translators.openconfig.vyos.openconfig_interfaces import interfaces
from ntc_rosetta.translators.openconfig.vyos.openconfig_network_instance.network_instances import (
    NetworkInstances,
)
from ntc_rosetta.translators.openconfig.vyos.openconfig_system.system import System

from yangify import translator


class VyOSTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = RequestList()
            self.result = self.root_result

        def post(self) -> None:
            # self.root_result = self.root_result.to_json()
            self.root_result = self.root_result.to_set()

    interfaces = interfaces.Interfaces
    network_instances = NetworkInstances
    system = System
