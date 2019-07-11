import json
import pathlib

import pytest

from yangson import exceptions
from yangson.enumerations import ContentType

basepath = pathlib.Path(__file__).parent


def get_data(model, filename):
    with open(basepath.joinpath("data", model, filename), "r") as f:
        return json.load(f)


class TestARP:
    def test_correct_config_ipv4(self, datamodel):
        data = datamodel.from_raw(get_data("arp", "correct_config_ipv4.json"))
        data.validate()

    def test_correct_config_ipv6(self, datamodel):
        data = datamodel.from_raw(get_data("arp", "correct_config_ipv6.json"))
        data.validate()

    def test_correct_state(self, datamodel):
        data = datamodel.from_raw(get_data("arp", "correct_state.json"))
        data.validate(ctype=ContentType.all)

    def test_missing_vrf(self, datamodel):
        data = datamodel.from_raw(get_data("arp", "missing_vrf.json"))
        with pytest.raises(exceptions.SemanticError) as e:
            data.validate()

    def test_vrf_mixed_up(self, datamodel):
        data = datamodel.from_raw(get_data("arp", "vrf_mixed_up.json"))
        with pytest.raises(exceptions.SemanticError) as e:
            data.validate(ctype=ContentType.all)
