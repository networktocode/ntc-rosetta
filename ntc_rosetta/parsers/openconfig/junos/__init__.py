from lxml import etree

from ntc_rosetta.parsers.openconfig.junos.openconfig_interfaces.interfaces import (
    Interfaces,
)
from ntc_rosetta.parsers.openconfig.junos.openconfig_network_instance.network_instances import (
    NetworkInstances,
)

from yangify import parser


class JunosParser(parser.RootParser):
    """
    JunosParser expects as native data a dictionary where the `dev_conf`
    key is reserved for the device configuration.
    """

    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native["dev_conf"] = etree.fromstring(
                self.root_native["dev_conf"]
            )
            self.native["dev_conf"] = self.root_native["dev_conf"]

    interfaces = Interfaces
    network_instances = NetworkInstances
