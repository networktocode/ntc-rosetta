from yangify.translator import Translator, TranslatorData, unneeded


class SingleTaggedConfig(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/single-tagged/config"
        )

    vlan_id = unneeded


class SingleTagged(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/single-tagged"
        )

    config = SingleTaggedConfig


class DoubleTaggedConfig(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/double-tagged/config"
        )

    inner_vlan_id = unneeded
    outer_vlan_id = unneeded


class DoubleTagged(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match/double-tagged"
        )

    config = DoubleTaggedConfig


class Match(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/"
            + "openconfig-vlan:vlan/match"
        )

    single_tagged = SingleTagged
    double_tagged = DoubleTagged


class Vlan(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan"

    match = Match
