from typing import List, Optional, cast

from yangify.parser import Parser, ParserData


class SwitchedVlanConfig(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-interfaces:interfaces/interface/"
            + "openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan/config"
        )

        def _interface_mode(self) -> Optional[str]:
            mode = self.native.xpath(
                "unit[name=0]/family/ethernet-switching/interface-mode"
            )
            if mode:
                return cast(str, mode[0].text.upper())
            else:
                return None

    def interface_mode(self) -> Optional[str]:
        return cast(Optional[str], self.yy._interface_mode())

    def access_vlan(self) -> Optional[int]:
        if self.yy._interface_mode() == "ACCESS":
            vlan = self.yy.native.xpath(
                "unit[name=0]/family/ethernet-switching/vlan/members"
            )
            if vlan:
                return int(vlan[0].text)
        return None

    def trunk_vlans(self) -> Optional[List[str]]:
        if self.yy._interface_mode() == "TRUNK":
            vlans = self.yy.native.xpath(
                "unit[name=0]/family/ethernet-switching/vlan/members"
            )
            if vlans:
                return [v.text for v in vlans]
        return None


class SwitchedVlan(Parser):
    class Yangify(ParserData):
        path = (
            "openconfig-interfaces:interfaces/interface/"
            + "openconfig-if-ethernet:ethernet/openconfig-vlan:switched-vlan"
        )

    config = SwitchedVlanConfig
