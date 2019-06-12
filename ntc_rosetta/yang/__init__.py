import pathlib

from yangson.datamodel import DataModel


base = pathlib.Path(__file__).parent
openconfig_lib = f"{base}/openconfig.json"
openconfig_path = [
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


def _get_openconfig_data_model() -> DataModel:
    return DataModel.from_file(openconfig_lib, openconfig_path)


def get_data_model(model: str = "openconfig") -> DataModel:
    """
    Returns an instantiated data model.
    """
    if model != "openconfig":
        raise ValueError(f"model {model} not recognized")
    return _get_openconfig_data_model()


__all__ = ("get_data_model",)
