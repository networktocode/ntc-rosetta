from ntc_rosetta.translators.openconfig.ios.openconfig_vlan import vlans

from yangify.translator import Translator, TranslatorData, unneeded


class NetowrkInstanceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance/config"

    name = unneeded


class NetworkInstance(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance"

        def pre_process_list(self) -> None:
            for element in self.to_remove:
                self.result.add_command(f"no vrf {element['name']}")

        def pre_process(self) -> None:
            if self.key == "default":
                return
            if self.replace:
                self.root_result[f"default vrf {self.key}"] = []
            path = f"vrf {self.key}"
            self.result = self.root_result.new_section(path)

        def post_process(self) -> None:
            if self.key == "default":
                return
            path = f"vrf {self.key}"
            if not self.result:
                self.root_result.pop_section(path)
            else:
                self.result.add_command("   exit\n!")

    config = NetowrkInstanceConfig
    vlans = vlans.Vlans

    name = unneeded


class NetworkInstances(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances"

        def pre_process(self) -> None:
            pass

    network_instance = NetworkInstance
