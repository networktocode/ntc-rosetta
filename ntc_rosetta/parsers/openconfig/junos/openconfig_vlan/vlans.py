from typing import Any, Dict, Iterator, Optional, Tuple, cast

from yangify.parser import Parser, ParserData


class VlanConfig(Parser):
    class Yangify(ParserData):
        path = "openconfig-network-instance:network-instances/network-instance/vlans/vlan/config"

    def vlan_id(self) -> int:
        return int(self.yy.key)

    def name(self) -> Optional[str]:
        return cast(Optional[str], self.yy.native.findtext("name"))

    def status(self) -> str:
        if self.yy.native.get("inactive"):
            return "SUSPENDED"
        else:
            return "ACTIVE"


class Vlan(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-network-instance:network-instances/network-instance/vlans/vlan"
        )

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for i in self.native.xpath("/configuration/vlans/vlan"):
                elem = i.findtext("vlan-id")
                if elem is None:
                    # QFX configuration may not contain vlan-id tag
                    continue
                yield elem, i

    config = VlanConfig

    def vlan_id(self) -> int:
        return int(self.yy.key)


class Vlans(Parser):
    class Yangify(ParserData):
        path = "openconfig-network-instance:network-instances/network-instance/vlans"

    vlan = Vlan
