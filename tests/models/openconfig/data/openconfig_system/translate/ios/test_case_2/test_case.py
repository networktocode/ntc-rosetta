"""
- Single DNS server
- Single user
"""

from tests.models.test_models import parse_path, translate
import pytest


@pytest.mark.parametrize("action", ["merge"])  # type: ignore
def test_translate(action: str) -> None:
    """Run a merge test with the provided action."""
    test_data = parse_path(__file__)
    translate(test_data.org, test_data.driver, test_data.path, action)
