from yangify.translator import Translator, TranslatorData


class Ethernet(Translator):
    class Yangify(TranslatorData):
        path = (
            "openconfig-interfaces:interfaces/interface/openconfig-if-ethernet:ethernet"
        )
