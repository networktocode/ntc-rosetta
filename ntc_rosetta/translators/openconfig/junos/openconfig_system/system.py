from lxml import etree
from yangify.translator import Translator, TranslatorData, unneeded


class ClockConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock/config"

    def timezone_name(self, value: str) -> None:
        etree.SubElement(self.yy.result, "time-zone").text = value


class Clock(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock"

    config = ClockConfig


class DnsConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/config"

    search = unneeded


class DnsServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server/config"

    address = unneeded
    port = unneeded


class DnsServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    ns = etree.SubElement(self.result, "name-server", delete="delete")
                    etree.SubElement(ns, "name").text = str(element.value["address"])

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "name-server")

    def address(self, value: str):
        etree.SubElement(self.yy.result, "name").text = value

    config = DnsServerConfig


class DnsServers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers"

    server = DnsServer


class Dns(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns"

    config = DnsConfig
    servers = DnsServers


class NtpServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server/config"


class NtpServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "server")

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    user = etree.SubElement(self.result, "server", delete="delete")
                    etree.SubElement(user, "name").text = str(element.value["address"])

    def address(self, value: str) -> None:
        etree.SubElement(self.yy.result, "name").text = value

    config = NtpServerConfig


class NtpServers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "ntp")

    server = NtpServer


class NtpConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/config"


class Ntp(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp"

    config = NtpConfig
    servers = NtpServers


class SshServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ssh-server/config"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "services")
            self.result = etree.SubElement(self.result, "ssh")

    def protocol_version(self, value: str) -> None:
        if value == "V2":
            etree.SubElement(self.yy.result, "protocol-version").text = value.lower()
        elif value == "V1":
            etree.SubElement(self.yy.result, "protocol-version").text = value.lower()
        else:
            etree.SubElement(self.yy.result, "protocol-version").text = "v2"

    def timeout(self, value: int) -> None:
        # Is this supported on Junos?
        # etree.SubElement(self.yy.result, "timeout").text = value
        return


class SshServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ssh-server"

    config = SshServerConfig


class AaaAuthenticationUserConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user/config"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "user")

    def username(self, value: str) -> None:
        etree.SubElement(self.yy.result, "name").text = value

    def role(self, value: str) -> None:
        etree.SubElement(self.yy.result, "class").text = value

    def password(self, value: str) -> None:
        self.yy.result = etree.SubElement(self.yy.result, "authentication")
        etree.SubElement(self.yy.result, "plain-text-password").text = value

    def password_hashed(self, value: str) -> None:
        self.yy.result = etree.SubElement(self.yy.result, "authentication")
        etree.SubElement(self.yy.result, "encrypted-password").text = value

    def ssh_key(self, value: str) -> None:
        self.yy.result = etree.SubElement(self.yy.result, "authentication")
        self.yy.result = etree.SubElement(self.yy.result, "ssh-rsa")
        etree.SubElement(self.yy.result, "name").text = value


class AaaAuthenticationUser(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def pre_process_list(self) -> None:
            self.result = etree.SubElement(self.result, "login")
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    user = etree.SubElement(self.result, "user", delete="delete")
                    etree.SubElement(user, "name").text = element.value["username"]

    config = AaaAuthenticationUserConfig


class AaaAuthenticationUsers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users"

    user = AaaAuthenticationUser


class AaaAuthentication(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication"

    users = AaaAuthenticationUsers


class AaaTacacsConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/tacacs/config"

    def secret_key(self, value: str) -> None:
        etree.SubElement(self.yy.result, "secret").text = value

    def source_address(self, value: str) -> None:
        etree.SubElement(self.yy.result, "source-address").text = value

    port = unneeded


class AaaTacacs(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/tacacs"

    config = AaaTacacsConfig


class AaaServerGroupServersServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server"

        def pre_process(self):
            self.result = etree.SubElement(self.result, "tacplus-server")

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    tacserver = etree.SubElement(
                        self.result, "tacplus-server", delete="delete"
                    )
                    etree.SubElement(tacserver, "name").text = element.value["address"]

    def address(self, value: str) -> None:
        etree.SubElement(self.yy.result, "name").text = value

    tacacs = AaaTacacs


class AaaServerGroupServers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers"

    server = AaaServerGroupServersServer


class AaaServerGroup(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group"

    servers = AaaServerGroupServers
    name = unneeded


class AaaServerGroups(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups"

    server_group = AaaServerGroup


class Aaa(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa"

    authentication = AaaAuthentication
    server_groups = AaaServerGroups


class SystemConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/config"

    def hostname(self, value: str) -> None:
        etree.SubElement(self.yy.result, "host-name").text = value


class System(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system"

        def pre_process(self) -> None:
            self.result = etree.SubElement(self.result, "system")  # type: ignore
            if self.replace:
                self.result.attrib["replace"] = "replace"

    config = SystemConfig
    ssh_server = SshServer
    aaa = Aaa
    clock = Clock
    ntp = Ntp
    dns = Dns
