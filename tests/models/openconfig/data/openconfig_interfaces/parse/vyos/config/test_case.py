from tests.models.test_models import parse_path, parser


def test_parser() -> None:
    """Run a merge test with the provided action."""
    test_data = parse_path(__file__)
    parser(test_data.org, test_data.model, test_data.driver, test_data.path)
