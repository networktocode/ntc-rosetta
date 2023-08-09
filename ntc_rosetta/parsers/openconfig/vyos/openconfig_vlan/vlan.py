from yangify.parser import ParserData, Parser


class SingleTaggedConfig(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/single-tagged/config"
        )

    def vlan_id(self):
        if isinstance(self.yy.key, str):
            return int(self.yy.key)
        return None


class DoubleTaggedConfig(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/double-tagged/config"
        )

    def inner_vlan_id(self):
        if isinstance(self.yy.key, tuple):
            return int(self.yy.key[1])
        return None

    def outer_vlan_id(self):
        if isinstance(self.yy.key, tuple):
            return int(self.yy.key[0])
        return None


class SingleTagged(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/single-tagged"
        )

    config = SingleTaggedConfig


class DoubleTagged(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/double-tagged"
        )

    config = DoubleTaggedConfig


class Match(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match"
        )

    single_tagged = SingleTagged
    double_tagged = DoubleTagged


class Vlan(Parser):
    class Yangify(ParserData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan"

    match = Match
