from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.ntc.junos import JunosParser as NTCJunosParser
from ntc_rosetta.parsers.openconfig.junos import JunosParser as OCJunosParser
from ntc_rosetta.translators.ntc.junos import JunosTranslator as NTCJunosTranslator
from ntc_rosetta.translators.openconfig.junos import (
    JunosTranslator as OCJunosTranslator,
)


class JunosDriverOpenconfig(Driver):
    parser = OCJunosParser
    translator = OCJunosTranslator
    datamodel_name = "openconfig"


class JunosDriverNTC(Driver):
    parser = NTCJunosParser
    translator = NTCJunosTranslator
    datamodel_namw = "ntc"
