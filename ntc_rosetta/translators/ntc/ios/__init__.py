from ntc_rosetta.translators.ntc.ios.ntc_vlan.vlan import Vlan

from yangify import translator
from yangify.translator.config_tree import ConfigTree


class NTCTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.result = self.root_result

        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    vlan = Vlan
