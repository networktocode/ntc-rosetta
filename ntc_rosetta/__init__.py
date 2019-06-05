from typing import Dict, Type

from ntc_rosetta.drivers import ios, junos
from ntc_rosetta.drivers.base import Driver


def get_driver(driver: str, model: str = "openconfig") -> Type[Driver]:
    """
    Returns a driver class to operate on a given device OS/model pair

    Arguments:
        model: Which model to retrieve, currently suppporting "openconfig" and "ntc"
    """
    mapping: Dict[str, Dict[str, Type[Driver]]] = {
        "openconfig": {
            "ios": ios.IOSDriverOpenconfig,
            "junos": junos.JunosDriverOpenconfig,
        },
        "ntc": {"ios": ios.IOSDriverNTC, "junos": junos.JunosDriverNTC},
    }
    return mapping[model][driver]
