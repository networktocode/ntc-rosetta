from typing import Optional

from yangify.translator import Translator, TranslatorData, unneeded


class VlanConfigVlans(Translator):
    class Yangify(TranslatorData):
        path = "/ntc-vlan:vlan/config/vlans"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(f"no vlan {element['vlan-id']}")

        def pre_process(self) -> None:
            if self.replace:
                self.root_result.add_command(f"no vlan {self.key}")
            self.result = self.root_result.new_section(f"vlan {self.key}")

        def post_process(self) -> None:
            if self.result:
                self.result.add_command("   exit\n!")
            else:
                self.root_result.pop_section(f"vlan {self.key}")

    vlan_id = unneeded

    def name(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   name {value}")
        else:
            self.yy.result.add_command(f"   no name")

    def active(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"   no shutdown")
        else:
            self.yy.result.add_command(f"   shutdown")


class VlanConfig(Translator):
    class Yangify(TranslatorData):
        path = "/ntc-vlan:vlan/config"

    vlans = VlanConfigVlans


class Vlan(Translator):
    class Yangify(TranslatorData):
        path = "/ntc-vlan:vlan"

    config = VlanConfig
