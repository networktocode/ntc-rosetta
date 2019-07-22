import json
import pathlib

import pytest

from yangson import exceptions

basepath = pathlib.Path(__file__).parent


def get_data(model, filename):
    with open(basepath.joinpath("data", model, filename), "r") as f:
        return json.load(f)


class TestVlan:
    def test_correct(self, datamodel):
        data = datamodel.from_raw(get_data("vlan", "correct.json"))
        data.validate()

    def test_missing_vlan_id(self, datamodel):
        data = datamodel.from_raw(get_data("vlan", "missing_vlan_id.json"))
        with pytest.raises(exceptions.SchemaError) as e:
            data.validate()

    def test_vlan_id_string(self, datamodel):
        with pytest.raises(exceptions.RawTypeError) as e:
            datamodel.from_raw(get_data("vlan", "vlan_id_string.json"))

    def test_vlan_id_wrong_number(self, datamodel):
        data = datamodel.from_raw(get_data("vlan", "vlan_id_wrong_number.json"))
        with pytest.raises(exceptions.YangTypeError) as e:
            data.validate()
