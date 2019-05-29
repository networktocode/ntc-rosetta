from ntc_rosetta.parsers.openconfig.ios.openconfig_interfaces.interfaces import (
    Interfaces,
)
from ntc_rosetta.parsers.openconfig.ios.openconfig_network_instance.network_instances import (
    NetworkInstances,
)

from yangify import parser
from yangify.parser.text_tree import parse_indented_config


class IOSParser(parser.RootParser):
    """
    IOSParser expects as native data a dictionary where the `dev_conf`
    key is reserved for the device configuration.
    """

    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native["dev_conf"] = parse_indented_config(
                self.root_native["dev_conf"].splitlines()
            )
            self.native["dev_conf"] = self.root_native["dev_conf"]

    interfaces = Interfaces
    network_instances = NetworkInstances
