from ntc_rosetta.parsers.openconfig.ios.openconfig_vlan import switched_vlan

from yangify.parser import Parser, ParserData


class Ethernet(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet"
        )

    switched_vlan = switched_vlan.SwitchedVlan
