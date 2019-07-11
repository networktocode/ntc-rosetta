from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.ntc.ios import NTCParser as NTCIOSParser
from ntc_rosetta.parsers.openconfig.ios import IOSParser as OCIOSParser
from ntc_rosetta.translators.ntc.ios import NTCTranslator as NTCIOSTranslator
from ntc_rosetta.translators.openconfig.ios import IOSTranslator as OCIOSTranslator


class IOSDriverOpenconfig(Driver):
    parser = OCIOSParser
    translator = OCIOSTranslator
    datamodel_name = "openconfig"


class IOSDriverNTC(Driver):
    parser = NTCIOSParser
    translator = NTCIOSTranslator
    datamodel_name = "ntc"
