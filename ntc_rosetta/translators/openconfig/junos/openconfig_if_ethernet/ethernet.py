from ntc_rosetta.translators.openconfig.junos.openconfig_vlan import switched_vlan

from yangify.translator import Translator, TranslatorData


class Ethernet(Translator):
    class Yangify(TranslatorData):
        path = (
            "openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet"
        )

    switched_vlan = switched_vlan.SwitchedVlan
