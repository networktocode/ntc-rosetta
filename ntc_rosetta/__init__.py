from typing import Dict, Type

from ntc_rosetta.drivers import ios, junos, vyos
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
            "vyos": vyos.VyOSDriverOpenconfig,
        },
        "ntc": {
            "ios": ios.IOSDriverNTC,
            "junos": junos.JunosDriverNTC,
            "vyos": vyos.VyOSDriverNTC,
        },
    }
    return mapping[model][driver]
