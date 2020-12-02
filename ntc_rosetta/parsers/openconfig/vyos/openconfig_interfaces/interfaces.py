from typing import Any, Dict, Iterator, Optional, Tuple, cast

from ntc_rosetta.parsers.openconfig.vyos.openconfig_if_ethernet import ethernet
from ntc_rosetta.parsers.openconfig.vyos.openconfig_vlan import vlan

from yangify.parser import Parser, ParserData


class SubinterfaceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config"

    def description(self) -> Optional[str]:
        return self.yy.native.get("description")

    def enabled(self) -> bool:
        return "disable" not in self.yy.native

    def index(self) -> int:
        if isinstance(self.yy.key, str):
            return int(self.yy.key)
        vlan_s = self.yy.key[0]
        vlan_c = self.yy.key[1]
        prepends = 4 - len(vlan_c)
        vlan_c = ("0" * prepends) + vlan_c
        return int(vlan_s + vlan_c)


class Subinterface(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"

        def extract_elements(self) -> Iterator[Tuple[str, Any]]:
            for k, v in self.native.get("vif", {}).items():
                yield k, v
            for k_s, v_s in self.native.get("vif-s", {}).items():
                # yield k_s, v_s
                for k_c, v_c in v_s.get("vif-c", {}).items():
                    yield (k_s, k_c), v_c

    config = SubinterfaceConfig
    vlan = vlan.Vlan

    def index(self) -> int:
        if isinstance(self.yy.key, str):
            return int(self.yy.key)
        vlan_s = self.yy.key[0]
        vlan_c = self.yy.key[1]
        prepends = 4 - len(vlan_c)
        vlan_c = ("0" * prepends) + vlan_c
        return int(vlan_s + vlan_c)


class Subinterfaces(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces"

    subinterface = Subinterface


class InterfaceConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/config"

    def description(self) -> Optional[str]:
        return self.yy.native.get("description")

    def enabled(self) -> bool:
        return "disable" not in self.yy.native

    def name(self) -> str:
        return cast(str, self.yy.key)

    def type(self) -> Optional[str]:
        if self.yy.key.startswith("eth"):
            return "iana-if-type:ethernetCsmacd"
        elif self.yy.key.startswith("lo"):
            return "iana-if-type:softwareLoopback"
        elif self.yy.key.startswith("bond"):
            return "iana-if-type:ieee8023adLag"
        elif self.yy.key.startswith("br"):
            return "iana-if-type:bridge"
        elif self.yy.key.startswith("macsec"):
            return "iana-if-type:macSecControlledIF"
        elif self.yy.key.startswith("tunnel"):
            return "iana-if-type:tunnel"
        else:
            raise Exception(f"don't know the type for {self.yy.key}")

    def mtu(self) -> Optional[int]:
        mtu = self.yy.native.get("mtu")
        return int(mtu) if mtu else None


class Interface(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface"

        def extract_elements(self) -> Iterator[Tuple[str, Any]]:
            if "interfaces" in self.native:
                for interfaces in self.native["interfaces"].values():
                    for k, v in interfaces.items():
                        yield k, v

    config = InterfaceConfig
    subinterfaces = Subinterfaces
    ethernet = ethernet.Ethernet

    def name(self) -> str:
        return cast(str, self.yy.key)


class Interfaces(Parser):
    interface = Interface

    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces"
        metadata = {"key": "dev_conf", "rpc": "showConfig"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]
