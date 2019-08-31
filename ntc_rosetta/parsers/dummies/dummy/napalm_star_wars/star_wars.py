from typing import Any, Dict, Iterator, Optional, Tuple, cast

from ntc_rosetta.helpers import json_helpers as jh

from yangify.parser import Parser, ParserData


class PersonalData(Parser):
    class Yangify(ParserData):
        path = "/napalm-star-wars:individual/personal-data"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for k, v in jh.query("vlan", self.native, default={}).items():
                if k == "#text":
                    continue
                yield k, cast(Dict[str, Any], v)

    def name(self) -> Optional[str]:
        v = jh.query('name."#text"', self.yy.native)
        if v is not None:
            return str(v)
        else:
            return None

    def age(self) -> int:
        return int(self.yy.key)

    def affiliation(self) -> bool:
        return not jh.query('shutdown."#standalone"', self.yy.native)


class Universe(Parser):
    class Yangify(ParserData):
        path = "/napalm-star-wars:universe/individual"
        metadata = {"key": "dev_conf", "command": "show running-config all"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]

    personal_data = PersonalData
