from lxml import etree
from yangify.translator import Translator, TranslatorData, unneeded


class Ipv4AddressConfig(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"
            "/openconfig-if-ip:ipv4/addresses/address/config"
        )

    def prefix_length(self, value: int) -> None:
        etree.SubElement(self.yy.result, "name").text = "{ip}/{prefix}".format(
            ip=self.yy.key, prefix=str(value)
        )

    ip = unneeded


class Ipv4Address(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"
            "/openconfig-if-ip:ipv4/addresses/address"
        )

        def pre_process_list(self) -> None:
            pass
            # TODO: implement this
            # if self.to_remove and not self.replace:
            #     for element in self.to_remove:
            #         unit = etree.SubElement(self.result, "address", delete="delete")
            #         etree.SubElement(unit, "ip").text = str(element.value["index"])

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "family")  # type: ignore
            self.result = etree.SubElement(self.result, "inet")
            self.result = etree.SubElement(self.result, "address")

    config = Ipv4AddressConfig

    ip = unneeded


class Ipv4Addresses(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"
            "/openconfig-if-ip:ipv4/addresses"
        )

    address = Ipv4Address


class Ipv4(Translator):
    class Yangify(TranslatorData):
        path = (
            "/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface"
            "/openconfig-if-ip:ipv4"
        )

    addresses = Ipv4Addresses
