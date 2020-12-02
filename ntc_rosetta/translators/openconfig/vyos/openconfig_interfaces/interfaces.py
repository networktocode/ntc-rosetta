from typing import Optional
from ntc_rosetta.translators.openconfig.vyos.openconfig_if_ethernet import ethernet
from ntc_rosetta.translators.openconfig.vyos.openconfig_vlan import vlan
from yangify.translator import Translator, TranslatorData, unneeded

TYPES = {
    "eth": "ethernet",
    "lo": "loopback",
    "bond": "bonding",
    "br": "bridge",
    "macsec": "macsec",
    "tunnel": "tunnel",
}


def get_if_type(name: str) -> str:
    types = [v for k, v in TYPES.items() if name.startswith(k)]
    if len(types) > 0:
        return types[0]
    else:
        raise Exception(f"don't know the type for {name}")


class SubinterfaceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config"

    index = unneeded

    def description(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.set(["description"], value, use_pre_path=True)
        else:
            self.yy.result.delete(["description"], "", use_pre_path=True)

    def enabled(self, value: Optional[bool]) -> None:
        if value:
            self.yy.result.delete(["disable"], "", use_pre_path=True)
        else:
            self.yy.result.set(["disable"], "", use_pre_path=True)


class Subinterface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    data = element.value
                    parent_key = self.keys[
                        "/openconfig-interfaces:interfaces/interface"
                    ]
                    if_type = get_if_type(parent_key)
                    vlan_found = False
                    try:
                        vlan_id = str(
                            data["openconfig-vlan:vlan"]["match"]["single-tagged"][
                                "config"
                            ]["vlan-id"]
                        )
                        self.result.delete(
                            ["interfaces", if_type, parent_key, "vif"], vlan_id
                        )
                        vlan_found = True
                    except KeyError:
                        pass
                    try:
                        inner_vlan_id = str(
                            data["openconfig-vlan:vlan"]["match"]["double-tagged"][
                                "config"
                            ]["inner-vlan-id"]
                        )
                        outer_vlan_id = str(
                            data["openconfig-vlan:vlan"]["match"]["double-tagged"][
                                "config"
                            ]["outer-vlan-id"]
                        )
                        self.result.delete(
                            [
                                "interfaces",
                                if_type,
                                parent_key,
                                "vif-s",
                                outer_vlan_id,
                                "vif-c",
                            ],
                            inner_vlan_id,
                        )
                        vlan_found = True
                    except KeyError:
                        pass
                    if not vlan_found:
                        raise Exception(
                            f"don't know the vlan tag(s) for subinterface {self.key}"
                        )
                    #     TODO: should check if this is the last inner vlan for outer vlan and delete outer if true

        def pre_process(self) -> None:
            data = self.candidate.goto(self.path).value
            parent_key = self.keys["/openconfig-interfaces:interfaces/interface"]
            if_type = get_if_type(parent_key)
            self.result.pre_path = ["interfaces", if_type, parent_key]
            vlan_found = False
            try:
                vlan_id = str(
                    data["openconfig-vlan:vlan"]["match"]["single-tagged"]["config"][
                        "vlan-id"
                    ]
                )
                self.result.pre_path.extend(["vif", vlan_id])
                vlan_found = True
            except KeyError:
                pass
            try:
                inner_vlan_id = str(
                    data["openconfig-vlan:vlan"]["match"]["double-tagged"]["config"][
                        "inner-vlan-id"
                    ]
                )
                outer_vlan_id = str(
                    data["openconfig-vlan:vlan"]["match"]["double-tagged"]["config"][
                        "outer-vlan-id"
                    ]
                )
                self.result.pre_path.extend(
                    ["vif-s", outer_vlan_id, "vif-c", inner_vlan_id]
                )
                vlan_found = True
            except KeyError:
                pass
            if not vlan_found:
                raise Exception(
                    f"don't know the vlan tag(s) for subinterface {self.key}"
                )

    index = unneeded
    config = SubinterfaceConfig
    vlan = vlan.Vlan


class Subinterfaces(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/subinterfaces"

    subinterface = Subinterface


class InterfaceConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface/config"

    name = unneeded
    type = unneeded

    def description(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.set(["description"], value, use_pre_path=True)
        else:
            self.yy.result.delete(["description"], "", use_pre_path=True)

    def enabled(self, value: Optional[bool]) -> None:
        if value:
            self.yy.result.delete(["disable"], "", use_pre_path=True)
        else:
            self.yy.result.set(["disable"], "", use_pre_path=True)

    def mtu(self, value: Optional[int]) -> None:
        if value:
            self.yy.result.set(["mtu"], str(value), use_pre_path=True)
        else:
            self.yy.result.delete(["mtu"], "", use_pre_path=True)


class Interface(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces/interface"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    if_type = get_if_type(element.value["name"])
                    self.result.delete(["interfaces", if_type], element.value["name"])

        def pre_process(self) -> None:
            if_type = get_if_type(self.key)
            if self.replace:
                self.result.delete(["interfaces", if_type], self.key)
            self.result.pre_path = ["interfaces", if_type, self.key]

    name = unneeded

    subinterfaces = Subinterfaces
    config = InterfaceConfig
    ethernet = ethernet.Ethernet


class Interfaces(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-interfaces:interfaces"

    interface = Interface
