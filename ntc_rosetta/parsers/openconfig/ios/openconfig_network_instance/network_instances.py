from typing import Any, Dict, Iterator, Tuple, cast

from ntc_rosetta.parsers.openconfig.ios.openconfig_vlan import vlans

from yangify.parser import Parser, ParserData


class NetowrkInstanceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances/network-instance/config"

    def name(self) -> str:
        return cast(str, self.yy.key)


class NetworkInstance(Parser):
    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances/network-instance"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            yield "default", self.root_native["dev_conf"]

    config = NetowrkInstanceConfig
    vlans = vlans.Vlans

    def name(self) -> str:
        return cast(str, self.yy.key)


class NetworkInstances(Parser):
    network_instance = NetworkInstance

    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances"
        metadata = {"key": "dev_conf", "command": "show running-config all"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]
