from typing import Any, Dict, Iterator, Optional, Tuple, cast

from ntc_rosetta.helpers import json_helpers as jh

from yangify.parser import Parser, ParserData


class VlanConfigVlans(Parser):
    class Yangify(ParserData):
        path = "/ntc-vlan:vlan/config/vlans"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for k, v in jh.query("vlan", self.native, default={}).items():
                if k == "#text":
                    continue
                yield k, cast(Dict[str, Any], v)

    def vlan_id(self) -> int:
        return int(self.yy.key)

    def name(self) -> Optional[str]:
        v = jh.query('name."#text"', self.yy.native)
        if v is not None:
            return str(v)
        else:
            return None

    def active(self) -> bool:
        return not jh.query('shutdown."#standalone"', self.yy.native)


class VlanConfig(Parser):
    class Yangify(ParserData):
        path = "/ntc-vlan:vlan/config"

    vlans = VlanConfigVlans


class Vlan(Parser):
    class Yangify(ParserData):
        path = "/ntc-vlan:vlan"
        metadata = {"key": "dev_conf", "command": "show running-config all"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]

    config = VlanConfig
