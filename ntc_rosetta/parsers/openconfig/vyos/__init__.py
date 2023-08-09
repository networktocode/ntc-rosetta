from yangify import parser

from ntc_rosetta.helpers.vyos import parse_config_tree
from ntc_rosetta.parsers.openconfig.vyos.openconfig_interfaces.interfaces import (
    Interfaces,
)
from ntc_rosetta.parsers.openconfig.vyos.openconfig_network_instance.network_instances import (
    NetworkInstances,
)
from ntc_rosetta.parsers.openconfig.vyos.openconfig_system.system import System


class VyOSParser(parser.RootParser):
    """
    VyOSParser expects as native data a dictionary where the `dev_conf`
    key is reserved for the device configuration.
    """

    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native["dev_conf"] = parse_config_tree(
                self.root_native["dev_conf"].splitlines()
            )
            # self.root_native["dev_conf"] = json.loads(self.root_native["dev_conf"])
            self.native["dev_conf"] = self.root_native["dev_conf"]

    interfaces = Interfaces
    network_instances = NetworkInstances
    system = System
