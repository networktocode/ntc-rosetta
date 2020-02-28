import ntc_rosetta
from yangson.exceptions import InstanceValueError

import pytest


def test_ios_system_replace_fail() -> None:
    """IOS does not support configuration replacement for all sections of the config.

    Test that the appropriate error is raised on system replace.
    """
    driver_class = ntc_rosetta.get_driver("ios", "openconfig")
    device = driver_class()
    with pytest.raises(InstanceValueError):
        device.merge({"openconfig-system:system": {}}, {}, replace=True)
