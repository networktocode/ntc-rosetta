from tests.models.test_models import parse_path, merge

import pytest


@pytest.mark.parametrize("action", ["merge", "replace"])  # type: ignore
def test_merge(action: str) -> None:
    """Run a merge test with the provided action."""
    test_data = parse_path(__file__)
    merge(test_data.org, test_data.driver, test_data.path, action)
