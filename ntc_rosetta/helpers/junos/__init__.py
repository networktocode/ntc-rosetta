"""Junos-specific helper functions"""
from typing import Dict


class delete_attr:
    """Allow a custom delete attribute to be set on XML tags

    This class is a callable that will return the default value of
    `delete="delete"` for delete RPC's.  In newer releases, this has
    been changed to `operation="delete"`.
    """

    attr: Dict[str, str] = {"delete": "delete"}

    def __new__(cls) -> Dict[str, str]:
        """Prevent class instantiation"""
        return cls.call()

    @classmethod
    def set_delete_attr(cls, attr: Dict[str, str]) -> None:
        """Set the attribute to a custom value."""
        cls.attr = attr

    @classmethod
    def call(cls) -> Dict[str, str]:
        """Return the delete attribute"""
        return cls.attr
