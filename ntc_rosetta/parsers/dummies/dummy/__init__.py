from ntc_rosetta.parsers.dummies.dummy.napalm_star_wars.star_wars import (
    Universe,
)

from yangify import parser
from yangify.parser.text_tree import parse_indented_config


class DummyParser(parser.RootParser):
    """
    DummyParser expects as native data a dictionary where the `dev_conf`
    key is reserved for the device configuration.
    """

    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native["dev_conf"] = parse_indented_config(
                self.root_native["dev_conf"].splitlines()
            )
            self.native["dev_conf"] = self.root_native["dev_conf"]

    universe = Universe
