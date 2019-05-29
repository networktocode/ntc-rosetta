from typing import Any, Dict, Iterator, Optional, Tuple, cast

from ntc_rosetta.helpers import json_helpers as jh

from yangify.parser import Parser, ParserData


class VlanConfig(Parser):
    class Yangify(ParserData):
        path = "openconfig-network-instance:network-instances/network-instance/vlans/vlan/config"

    def vlan_id(self) -> int:
        return int(self.yy.key)

    def name(self) -> Optional[str]:
        v = jh.query('name."#text"', self.yy.native)
        if v is not None:
            return str(v)
        else:
            return None

    def status(self) -> str:
        if jh.query('shutdown."#standalone"', self.yy.native):
            return "SUSPENDED"
        else:
            return "ACTIVE"


class Vlan(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-network-instance:network-instances/network-instance/vlans/vlan"
        )

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for k, v in jh.query("vlan", self.native, default={}).items():
                if k == "#text":
                    continue
                yield k, cast(Dict[str, Any], v)

    config = VlanConfig

    def vlan_id(self) -> int:
        return int(self.yy.key)


class Vlans(Parser):
    class Yangify(ParserData):
        path = "openconfig-network-instance:network-instances/network-instance/vlans"

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]

    vlan = Vlan
