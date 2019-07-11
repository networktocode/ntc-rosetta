from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.ntc.ios import NTCParser as NTCIOSParser
from ntc_rosetta.parsers.openconfig.ios import IOSParser as OCIOSParser
from ntc_rosetta.translators.ntc.ios import NTCTranslator as NTCIOSTranslator
from ntc_rosetta.translators.openconfig.ios import IOSTranslator as OCIOSTranslator
from ntc_rosetta.yang import get_data_model


class IOSDriverOpenconfig(Driver):
    parser = OCIOSParser
    translator = OCIOSTranslator
    datamodel = get_data_model("openconfig")


class IOSDriverNTC(Driver):
    parser = NTCIOSParser
    translator = NTCIOSTranslator
    datamodel = get_data_model("ntc")
