from typing import Any, Dict, Iterator, Optional, Tuple, cast

from ntc_rosetta.parsers.openconfig.junos.openconfig_if_ethernet import ethernet

from yangify.parser import Parser, ParserData


class SubinterfaceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config"

    def description(self) -> Optional[str]:
        return cast(Optional[str], self.yy.native.findtext("description"))

    def index(self) -> int:
        return int(self.yy.key)


class Subinterface(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"

        def extract_elements(self) -> Iterator[Tuple[str, Any]]:
            for i in self.native.xpath("unit"):
                yield i.findtext("name"), i

    config = SubinterfaceConfig

    def index(self) -> int:
        return int(self.yy.key)


class Subinterfaces(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces"

    subinterface = Subinterface


class InterfaceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/config"

    def description(self) -> Optional[str]:
        # configuration really is under units/subifaces
        pass

    def enabled(self) -> bool:
        return self.yy.native.find("disable") is None

    def name(self) -> str:
        return cast(str, self.yy.key)

    def type(self) -> Optional[str]:
        if any(
            [self.yy.key.startswith(prefix) for prefix in ["ge", "xe", "et", "fxp"]]
        ):
            return "iana-if-type:ethernetCsmacd"
        elif self.yy.key.startswith("lo"):
            return "iana-if-type:softwareLoopback"
        elif self.yy.key.startswith("ae"):
            return "iana-if-type:ieee8023adLag"
        elif self.yy.key.startswith("irb"):
            return "iana-if-type:l3ipvlan"
        else:
            raise Exception(f"don't know the type for {self.yy.key}")


class Interface(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface"

        def extract_elements(self) -> Iterator[Tuple[str, Any]]:
            for i in self.native.xpath("/configuration/interfaces/interface"):
                yield i.findtext("name"), i

    config = InterfaceConfig
    subinterfaces = Subinterfaces
    ethernet = ethernet.Ethernet

    def name(self) -> str:
        return cast(str, self.yy.key)


class Interfaces(Parser):
    interface = Interface

    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces"
        metadata = {"key": "dev_conf", "rpc": "get-config"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]
