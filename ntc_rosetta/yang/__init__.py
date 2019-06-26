import pathlib

from yangson.datamodel import DataModel


BASEPATH = pathlib.Path(__file__).parent
OPENCONFIG_LIB = f"{BASEPATH}/openconfig.json"
OPENCONFIG_PATH = [
    BASEPATH.joinpath("YangModels/standard/ietf/RFC"),
    BASEPATH.joinpath("openconfig/release/models"),
    BASEPATH.joinpath("openconfig/release/models/acl"),
    BASEPATH.joinpath("openconfig/release/models/aft"),
    BASEPATH.joinpath("openconfig/release/models/bgp"),
    BASEPATH.joinpath("openconfig/release/models/interfaces"),
    BASEPATH.joinpath("openconfig/release/models/isis"),
    BASEPATH.joinpath("openconfig/release/models/mpls"),
    BASEPATH.joinpath("openconfig/release/models/multicast"),
    BASEPATH.joinpath("openconfig/release/models/network-instance"),
    BASEPATH.joinpath("openconfig/release/models/local-routing"),
    BASEPATH.joinpath("openconfig/release/models/ospf"),
    BASEPATH.joinpath("openconfig/release/models/policy"),
    BASEPATH.joinpath("openconfig/release/models/policy-forwarding"),
    BASEPATH.joinpath("openconfig/release/models/rib"),
    BASEPATH.joinpath("openconfig/release/models/segment-routing"),
    BASEPATH.joinpath("openconfig/release/models/types"),
    BASEPATH.joinpath("openconfig/release/models/vlan"),
]


def _get_openconfig_data_model() -> DataModel:
    return DataModel.from_file(OPENCONFIG_LIB, OPENCONFIG_PATH)


def get_data_model(model: str = "openconfig") -> DataModel:
    """
    Returns an instantiated data model.
    """
    if model != "openconfig":
        raise ValueError(f"model {model} not recognized")
    return _get_openconfig_data_model()


__all__ = ("get_data_model",)
