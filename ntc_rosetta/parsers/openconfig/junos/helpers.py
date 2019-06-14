"""Helper for junos parsers"""
from typing import List


def resolve_vlan_ids(vlans: List, root) -> List[int]:
    """Resolve named vlans from /configuration/vlans/vlan path"""
    rv = list()
    for vlan in vlans:
        if vlan.text.isnumeric():
            rv.append(int(vlan.text))
            continue
        elem = root["dev_conf"].xpath(
            "//vlan[name/text()='{member}']/vlan-id".format(member=vlan.text)
        )
        if elem is not None and len(elem):
            rv.append(int(elem[0].text))
    return rv
