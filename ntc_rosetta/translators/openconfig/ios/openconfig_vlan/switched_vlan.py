from typing import List, Optional

from yangify.translator import Translator, TranslatorData


class SwitchedVlanConfig(Translator):
    class Yangify(TranslatorData):
        path = (
            "openconfig-interfaces:interfaces/interface/"
            + "openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
        )

    def interface_mode(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   switchport mode {value.lower()}")
        else:
            self.yy.result.add_command("   switchport mode access")

    def access_vlan(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   switchport access vlan {value}")
        else:
            self.yy.result.add_command("   switchport access vlan 1")

    def trunk_vlans(self, value: Optional[List[str]]) -> None:
        if value:
            vlans_str = ",".join([str(v) for v in value])
            self.yy.result.add_command(f"   switchport trunk allowed vlan {vlans_str}")
        else:
            self.yy.result.add_command("   switchport trunk allowed vlan 1")


class SwitchedVlan(Translator):
    class Yangify(TranslatorData):
        path = (
            "openconfig-interfaces:interfaces/interface/"
            + "openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan"
        )

    config = SwitchedVlanConfig
