from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.ntc.junos import JunosParser as NTCJunosParser
from ntc_rosetta.parsers.openconfig.junos import JunosParser as OCJunosParser
from ntc_rosetta.translators.ntc.junos import JunosTranslator as NTCJunosTranslator
from ntc_rosetta.translators.openconfig.junos import (
    JunosTranslator as OCJunosTranslator,
)
from ntc_rosetta.yang import get_data_model


class JunosDriverOpenconfig(Driver):
    parser = OCJunosParser
    translator = OCJunosTranslator
    datamodel = get_data_model("openconfig")


class JunosDriverNTC(Driver):
    parser = NTCJunosParser
    translator = NTCJunosTranslator
    datamodel = get_data_model("ntc")
