from typing import Any, Dict, Iterator, Tuple, cast

from yangify.parser import Parser, ParserData


class NetworkInstanceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances/network-instance/config"

    def name(self) -> str:
        return cast(str, self.yy.key)

    def description(self) -> str:
        return self.yy.native.get("description")


class NetworkInstance(Parser):
    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances/network-instance"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            yield "default", self.root_native["dev_conf"]
            if "vrf" in self.native:
                for k, v in self.native["vrf"]["name"].items():
                    yield k, v

    config = NetworkInstanceConfig

    def name(self) -> str:
        return cast(str, self.yy.key)


class NetworkInstances(Parser):
    class Yangify(ParserData):
        path = "/openconfig-network-instance:network-instances"
        metadata = {"key": "dev_conf", "rpc": "showConfig"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]

    network_instance = NetworkInstance
