from typing import Optional

from yangify.translator import Translator, TranslatorData, unneeded


class NetworkInstanceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance/config"

    name = unneeded

    def description(self, value: Optional[str]) -> None:
        self.yy.result.set(["description"], value, use_pre_path=True)


class NetworkInstance(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance"

        def pre_process_list(self) -> None:
            for element in self.to_remove:
                self.result.delete(["vrf", "name"], element.value)

        def pre_process(self) -> None:
            if self.key == "default":
                return
            if self.replace:
                self.result.delete(["vrf", "name"], self.key)
            self.result.set(["vrf", "name"], self.key)
            self.result.pre_path = ["vrf", "name", self.key]

    config = NetworkInstanceConfig
    vlans = unneeded
    name = unneeded


class NetworkInstances(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances"

    network_instance = NetworkInstance
