from typing import Any, Dict, List, Optional

from ntc_rosetta.yang import get_data_model

from yangify.parser import RootParser
from yangify.translator import RootTranslator

from yangson.datamodel import DataModel
from yangson.instance import RootNode
from yangson.instvalue import Value
from yangson.typealiases import RawValue


class ParseResult:
    """
    Result of parsing a configuration

    Attributes:
        root: Root of the response
        datamodel: Datamodel related to the parsed object
    """

    def __init__(self, root: RootNode, datamodel: DataModel) -> None:
        self.root = root
        self.datamodel = datamodel

    def raw_value(self) -> RawValue:
        """
        Parsed data in python's native datastructures (dicts, lists, strings, etc)
        """
        return self.root.raw_value()

    def peek(self, path: str) -> Optional[Value]:
        """
        Return the value in the given path (YANG)
        """
        instp = self.datamodel.parse_resource_id(path)
        return self.root.peek(instp)


class Driver:
    """
    Parent class used to operate on models and native datastructures

    The class has a few class attributes that need to be overriden by
    classes inheriting from this class.

    Attributes:
        parser: Class attribute to defines which ``yangify.parser.RootParser`` to use
            when parsing native data
        translator: Class attribute to defines which ``yangify.translator.RootParser`` to use
            when translating YANG models to native data
        datamodel: Class attribute that defines which ``yangson.datamodel.DataModel`` the
            parser and translator can operate on.
    """

    parser = RootParser
    translator = RootTranslator
    datamodel_name = ""
    _datamodel: Optional[DataModel] = None

    @classmethod
    def get_datamodel(cls) -> DataModel:
        if cls._datamodel is None:
            cls._datamodel = get_data_model(cls.datamodel_name)
        return cls._datamodel

    def parse(
        self,
        native: Optional[Dict[str, Any]] = None,
        validate: bool = True,
        include: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None,
    ) -> ParseResult:
        """
        Parser native data and maps it into an object conforming to the datamodel.

        Args:
            native: native data extracted from a device
            validate: whether to validate the model or not
            include: if specified only return data matching the YANG paths here
            excldue: if specify exclude data matching the YANG paths here
        """
        native = native or {}
        parser = self.parser(
            self.get_datamodel(), native, include=include, exclude=exclude
        )
        root = parser.process(validate=validate)
        return ParseResult(root, self.get_datamodel())

    def translate(self, candidate: Dict[str, Any], replace: bool = False) -> Any:
        """
        Translates data conforming to the model into native configuration the device understands.

        Arguments:
            candidate: Data to translate (must conform to the datamodel of the driver)
            replace: Whether to return a list of commands that reinitializes blocks
                (i.e. defaulting an interface)
        """
        translator = self.translator(
            self.get_datamodel(), candidate=candidate, replace=replace
        )
        return translator.process()

    def merge(
        self, candidate: Dict[str, Any], running: Dict[str, Any], replace: bool = False
    ) -> Any:
        """
        Given two objects conforming to a data model compute the needed native commands
        to converge the configurations.

        Arguments:
            candidate: Desired configuration (must conform to the datamodel of the driver)
            running: Original configuration (must conform to the datamodel of the driver)
            replace: Whether to return a list of commands that reinitializes blocks
                (i.e. defaulting an interface)
        """
        translator = self.translator(
            self.get_datamodel(), candidate=candidate, running=running, replace=replace
        )
        return translator.process()
