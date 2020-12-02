from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.ntc.vyos import VyOSParser as NTCVyOSParser
from ntc_rosetta.parsers.openconfig.vyos import VyOSParser as OCVyOSParser
from ntc_rosetta.translators.ntc.vyos import VyOSTranslator as NTCVyOSTranslator
from ntc_rosetta.translators.openconfig.vyos import VyOSTranslator as OCVyOSTranslator


class VyOSDriverOpenconfig(Driver):
    parser = OCVyOSParser
    translator = OCVyOSTranslator
    datamodel_name = "openconfig"


class VyOSDriverNTC(Driver):
    parser = NTCVyOSParser
    translator = NTCVyOSTranslator
    datamodel_name = "ntc"
