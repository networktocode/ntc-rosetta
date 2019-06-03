import json
import pathlib
from typing import Any, Dict, List, Tuple

import ntc_rosetta

import pytest


filters: Dict[str, Dict[str, List[str]]] = {
    "openconfig-interfaces": {
        "include": [
            "/openconfig-interfaces:interfaces/interface/name",
            "/openconfig-interfaces:interfaces/interface/config",
            "/openconfig-interfaces:interfaces/interface/state",
            "/openconfig-interfaces:interfaces/interface/hold-time",
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/index",
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config",
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state",
        ],
        "exclude": [],
    },
    "openconfig-vlan": {
        "include": [
            "/openconfig-interfaces:interfaces",
            "/openconfig-network-instance:network-instances/network-instance/name",
            "/openconfig-network-instance:network-instances/network-instance/config",
            "/openconfig-network-instance:network-instances/network-instance/vlans",
        ],
        "exclude": [],
    },
}


def get_test_cases(test: str) -> Dict[str, Any]:
    base = pathlib.Path(__file__).parent

    test_cases: List[Tuple[str, str, pathlib.Path]] = []
    ids: List[str] = []
    for model_path in base.joinpath(f"data").iterdir():
        model = model_path.name
        for driver_path in sorted(model_path.joinpath(test).iterdir()):
            driver = driver_path.name
            for test_case_path in sorted(driver_path.iterdir()):
                test_case = test_case_path.name
                ids.append(f"{model}_{driver}_{test_case}")
                test_cases.append((model, driver, test_case_path))
    return {
        "argnames": "model,driver,test_case_path",
        "argvalues": test_cases,
        "ids": ids,
    }


class Test:
    @pytest.mark.parametrize(**get_test_cases("parse"))  # type: ignore
    def test_parser(
        self, model: str, driver: str, test_case_path: pathlib.Path
    ) -> None:
        device_config_files = []
        result_files = []
        for file_path in test_case_path.iterdir():
            if file_path.is_file():
                if file_path.name.startswith("dev_conf"):
                    device_config_files.append(file_path)
                elif file_path.name.startswith("result"):
                    result_files.append(file_path)
        # Assuming there is only a single testcase for this parser.
        if len(device_config_files) == 1:
            self._run_parser_test(
                model, driver, device_config_files[0], result_files[0]
            )
        else:
            for device_config, result in zip(
                sorted(device_config_files), sorted(result_files)
            ):
                if "passes" in device_config.name:
                    self._run_parser_test(model, driver, device_config, result)
                elif "fails" in device_config.name:
                    with pytest.raises(AssertionError):
                        self._run_parser_test(model, driver, device_config, result)
                elif "_raises_" in device_config.name:
                    exception_name = device_config.name.split("_raises_")[-1]
                    with pytest.raises(eval(exception_name)):
                        self._run_parser_test(model, driver, device_config, result)

    @staticmethod
    def _run_parser_test(
        model: str, driver: str, device_config: pathlib.Path, result: pathlib.Path
    ) -> None:
        with open(device_config, "r") as f:
            dev_conf = f.read()
        with open(result, "r") as f:
            structured = json.load(f)

        driver_class = ntc_rosetta.get_driver(driver)
        device = driver_class()

        parsed_obj = device.parse(
            native={"dev_conf": dev_conf},
            validate=False,
            include=filters[model]["include"],
            exclude=filters[model]["exclude"],
        )
        print(json.dumps(parsed_obj.raw_value()))
        assert parsed_obj.raw_value() == structured, json.dumps(parsed_obj.raw_value())

    def _test_translate(
        self, driver: str, test_case_path: pathlib.Path, mode: str
    ) -> None:
        with open(test_case_path.joinpath("data.json"), "r") as f:
            candidate = json.load(f)
        with open(test_case_path.joinpath(f"res_{mode}"), "r") as f:
            expected = f.read()
        driver_class = ntc_rosetta.get_driver(driver)
        device = driver_class()
        config = device.translate(candidate, replace=mode == "replace")
        assert config == expected

    @pytest.mark.parametrize(**get_test_cases("translate"))  # type: ignore
    def test_translate_merge(
        self, model: str, driver: str, test_case_path: pathlib.Path
    ) -> None:
        self._test_translate(driver, test_case_path, "merge")

    @pytest.mark.parametrize(**get_test_cases("translate"))  # type: ignore
    def test_translate_replace(
        self, model: str, driver: str, test_case_path: pathlib.Path
    ) -> None:
        self._test_translate(driver, test_case_path, "replace")

    def _test_merge(self, driver: str, test_case_path: pathlib.Path, mode: str) -> None:
        with open(test_case_path.joinpath("data_candidate.json"), "r") as f:
            candidate = json.load(f)
        with open(test_case_path.joinpath("data_running.json"), "r") as f:
            running = json.load(f)
        with open(test_case_path.joinpath(f"res_{mode}"), "r") as f:
            expected = f.read()
        driver_class = ntc_rosetta.get_driver(driver)
        device = driver_class()
        res_merge = device.merge(candidate, running, replace=mode == "replace")
        assert res_merge == expected

    @pytest.mark.parametrize(**get_test_cases("merge"))  # type: ignore
    def test_merge_merge(
        self, model: str, driver: str, test_case_path: pathlib.Path
    ) -> None:
        self._test_merge(driver, test_case_path, "merge")

    @pytest.mark.parametrize(**get_test_cases("merge"))  # type: ignore
    def test_merge_replace(
        self, model: str, driver: str, test_case_path: pathlib.Path
    ) -> None:
        self._test_merge(driver, test_case_path, "replace")
