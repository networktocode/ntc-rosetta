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
            parsed_xml = etree.fromstring(self.root_native["dev_conf"])
            if parsed_xml.tag != "configuration":
                parsed_xml = parsed_xml.find('configuration')
                if not parsed_xml: 
                    raise AttributeError("Unable to locate 'configuration' tag in XML blob")                        
            self.root_native["dev_conf"] = parsed_xml
            self.native["dev_conf"] = self.root_native["dev_conf"]

    interfaces = Interfaces
    network_instances = NetworkInstances
