"""
- Multiple DNS servers
- Multiple users
- Check bad ssh hash
"""
import ntc_rosetta
from tests.models.test_models import parse_path, translate
from yangson.exceptions import UnexpectedInput
import pytest


@pytest.mark.parametrize("action", ["merge"])  # type: ignore
def test_translate(action: str) -> None:
    """Run a merge test with the provided action."""
    test_data = parse_path(__file__)
    translate(test_data.org, test_data.driver, test_data.path, action)


def test_ios_translate_ssh_hash_fail() -> None:
    """Assert that a supported hash type is present"""
    fail = {
        "openconfig-system:system": {
            "aaa": {
                "authentication": {
                    "users": {
                        "user": [
                            {
                                "username": "developer",
                                "config": {
                                    "username": "developer",
                                    # $7 is an in valid value
                                    "password-hashed": "$7$foobar",
                                    "role": "15",
                                },
                            }
                        ]
                    }
                }
            }
        }
    }
    driver_class = ntc_rosetta.get_driver("ios", "openconfig")
    device = driver_class()
    with pytest.raises(UnexpectedInput):
        device.translate(fail)
