import re

from lxml import etree


def find_or_create(root: etree.Element, xpath: str) -> etree.Element:
    """
    Return a subelement or create if it doesn't exist.

    Args:
        root: Root of the object
        xpath: xpath to apply to the root object
    """
    path = xpath.split("/")
    regex = re.compile(
        r"(?P<query_path>\w+)\[(?P<name>\w+)='*(?P<identifier>(\w+)[-*|\d*|\/*|]*)'*\]|(?!\[)(?P<path>\w+)"  # noqa
    )
    element = root
    for match in regex.findall(xpath)[1:]:
        query_path, id_name, id_value, _, path = match
        if id_name:
            filtered = element.find(f"{query_path}[{id_name}='{id_value}']")
            if filtered is None:
                element = etree.SubElement(element, query_path)
                element = etree.SubElement(element, id_name)
                element.text = id_value
                element = element.getparent()
            else:
                element = filtered
        elif path:
            filtered = element.find(f"{path}")
            if filtered is None:
                element = etree.SubElement(element, path)
            else:
                element = filtered
    return element
