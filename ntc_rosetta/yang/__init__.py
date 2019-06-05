import pathlib

from yangson.datamodel import DataModel


def _get_openconfig_data_model() -> DataModel:
    base = pathlib.Path(__file__).parent
    lib = f"{base}/openconfig.json"
    path = [
        base.joinpath("YangModels/standard/ietf/RFC"),
        base.joinpath("openconfig/release/models"),
        base.joinpath("openconfig/release/models/acl"),
        base.joinpath("openconfig/release/models/aft"),
        base.joinpath("openconfig/release/models/bgp"),
        base.joinpath("openconfig/release/models/interfaces"),
        base.joinpath("openconfig/release/models/isis"),
        base.joinpath("openconfig/release/models/mpls"),
        base.joinpath("openconfig/release/models/multicast"),
        base.joinpath("openconfig/release/models/network-instance"),
        base.joinpath("openconfig/release/models/local-routing"),
        base.joinpath("openconfig/release/models/ospf"),
        base.joinpath("openconfig/release/models/policy"),
        base.joinpath("openconfig/release/models/policy-forwarding"),
        base.joinpath("openconfig/release/models/rib"),
        base.joinpath("openconfig/release/models/segment-routing"),
        base.joinpath("openconfig/release/models/types"),
        base.joinpath("openconfig/release/models/vlan"),
    ]
    return DataModel.from_file(lib, path)


def _get_ntc_data_model() -> DataModel:
    base = pathlib.Path(__file__).parent
    lib = f"{base}/ntc-yang-models/models/ntc-models-library.json"
    path = [
        base.joinpath("ntc-yang-models/models/arp"),
        base.joinpath("ntc-yang-models/models/ietf"),
        base.joinpath("ntc-yang-models/models/system"),
        base.joinpath("ntc-yang-models/models/types"),
        base.joinpath("ntc-yang-models/models/vlan"),
        base.joinpath("ntc-yang-models/models/vrf"),
    ]
    return DataModel.from_file(lib, path)


def get_data_model(model: str = "openconfig") -> DataModel:
    """
    Returns an instantiated data model.
    """
    if model == "openconfig":
        return _get_openconfig_data_model()
    elif model == "ntc":
        return _get_ntc_data_model()
    else:
        raise ValueError(f"model {model} not recognized")


__all__ = ("get_data_model",)
