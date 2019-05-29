from ntc_rosetta.translators.openconfig.junos.openconfig_vlan import vlans

from yangify.translator import Translator, TranslatorData, unneeded


class NetowrkInstanceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance/config"

    name = unneeded


class NetworkInstance(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances/network-instance"

        def pre_process_list(self) -> None:
            return None

        def pre_process(self) -> None:
            return None

    config = NetowrkInstanceConfig
    vlans = vlans.Vlans

    name = unneeded


class NetworkInstances(Translator):
    network_instance = NetworkInstance

    class Yangify(TranslatorData):
        path = "/openconfig-network-instance:network-instances"

        def pre_process(self) -> None:
            return None
