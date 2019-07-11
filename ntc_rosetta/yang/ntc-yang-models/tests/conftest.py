import pathlib

import pytest

import yangson


@pytest.fixture(scope="session", autouse=True)
def datamodel(request):
    basepath = pathlib.Path(__file__).parent.joinpath("..", "models")
    path = [p for p in basepath.iterdir() if p.is_dir() and not p.name.startswith(".")]

    ylpath = pathlib.Path(__file__).parent.joinpath(
        "..", "models", "ntc-models-library.json"
    )

    with open(ylpath, "r") as f:
        mod = f.read()

    return yangson.DataModel(mod, mod_path=path)
