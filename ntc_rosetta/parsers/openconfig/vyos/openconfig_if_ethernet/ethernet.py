from yangify.parser import Parser, ParserData


class Ethernet(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet"
        )
