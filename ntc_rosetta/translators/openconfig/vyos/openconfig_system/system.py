from typing import List

from yangify.translator import Translator, TranslatorData, unneeded


class AaaRadiusConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/radius/config"

    def secret_key(self, value: str) -> None:
        self.yy.result.set(["key"], value, use_pre_path=True)

    def source_address(self, value: str) -> None:
        self.yy.result.set(["system", "login", "radius", "source-address"], value)

    def auth_port(self, value: int) -> None:
        self.yy.result.set(["port"], str(value), use_pre_path=True)


class AaaRadius(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/radius"

    config = AaaRadiusConfig


class AaaServerGroupServersServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.delete(
                        ["system", "login", "radius", "server"],
                        element.value["address"],
                    )

        def pre_process(self):
            if self.replace:
                self.result.delete(["system", "login", "radius", "server"], self.key)
            self.result.pre_path = ["system", "login", "radius", "server", self.key]

    address = unneeded
    radius = AaaRadius


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


class AaaAuthenticationUserConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user/config"

    username = unneeded
    role = unneeded

    def password(self, value: str) -> None:
        if value:
            self.yy.result.set(["plaintext-password"], value, use_pre_path=True)

    def password_hashed(self, value: str) -> None:
        if value:
            self.yy.result.set(["encrypted-password"], value, use_pre_path=True)

    def ssh_key(self, value: str) -> None:
        if value:
            self.yy.result.set(
                ["public-keys", self.yy.key, "key"], value, use_pre_path=True
            )
            self.yy.result.set(
                ["public-keys", self.yy.key, "type"], "ssh-rsa", use_pre_path=True
            )


class AaaAuthenticationUser(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.delete(
                        ["system", "login", "user"], element.value["username"]
                    )

        def pre_process(self) -> None:
            if self.replace:
                self.result.delete(["system", "login", "user"], self.key)
            self.result.pre_path = [
                "system",
                "login",
                "user",
                self.key,
                "authentication",
            ]

    username = unneeded
    config = AaaAuthenticationUserConfig


class AaaAuthenticationUsers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users"

    user = AaaAuthenticationUser


class AaaAuthentication(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication"

    users = AaaAuthenticationUsers


class AaaAuthorizationConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authorization/config"

    authorization_method = unneeded


class AaaAuthorization(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authorization"

    config = AaaAuthorizationConfig


class Aaa(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa"

    authentication = AaaAuthentication
    authorization = AaaAuthorization
    server_groups = AaaServerGroups


class ConsoleSelectorConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/logging/console/selectors/selector/config"

    facility = unneeded
    severity = unneeded


class ConsoleSelector(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/logging/console/selectors/selector"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.delete(["facility"], element["facility"])

    _facility_val = None
    _severity_val = None

    def facility(self, value: str) -> None:
        if self._severity_val:
            self.yy.result.set(
                ["facility", value, "level"], self._severity_val, use_pre_path=True
            )
        else:
            self._facility_val = value

    def severity(self, value: str) -> None:
        if self._facility_val:
            self.yy.result.set(
                ["facility", self._facility_val, "level"], value, use_pre_path=True
            )
        else:
            self._severity_val = value

    config = ConsoleSelectorConfig


class ConsoleSelectors(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/logging/console/selectors"

    # TODO: Can't be implemented, due to possible bug in Yangson, when using identityref as list key
    # selector = ConsoleSelector


class Console(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/logging/console"

        def pre_process(self) -> None:
            self.result.pre_path = ["system", "syslog", "console"]

    selectors = ConsoleSelectors


class Logging(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/logging"

    console = Console
    # remote_servers = unneeded  # RemoteServers


class SshServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ssh-server/config"

    def enable(self, value: bool) -> None:
        if value:
            self.yy.result.set(["service", "ssh"], "")

    protocol_version = unneeded
    timeout = unneeded
    rate_limit = unneeded
    session_limit = unneeded


class SshServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ssh-server"

    config = SshServerConfig


class NtpServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server/config"

    address = unneeded

    def prefer(self, value: bool) -> None:
        if value:
            self.yy.result.set(["prefer"], "", use_pre_path=True)


class NtpServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.delete(
                        ["system", "ntp", "server"], element.value["address"]
                    )

        def pre_process(self) -> None:
            if self.replace:
                self.result.delete(["system", "ntp", "server"], self.key)

    def address(self, value: str) -> None:
        self.yy.result.set(["system", "ntp", "server"], value)
        self.yy.result.pre_path = ["system", "ntp", "server", value]

    config = NtpServerConfig


class NtpServers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers"

    server = NtpServer


class NtpConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/config"

    enabled = unneeded


class Ntp(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp"

    config = NtpConfig
    servers = NtpServers


class HostEntryConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:/system/dns/host-entries/host-entry/config"

    hostname = unneeded

    def alias(self, value: List[str]) -> None:
        # VyOS only supports one alias, so we return the first
        self.yy.result.set(["alias"], value[0], use_pre_path=True)

    def ipv4_address(self, value: List[str]) -> None:
        # VyOS only supports one address, so we return the first
        self.yy.result.set(["inet"], value[0], use_pre_path=True)

    def ipv6_address(self, value: List[str]) -> None:
        # VyOS only supports one address, so we return the first
        self.yy.result.set(["inet"], value[0], use_pre_path=True)


class HostEntry(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:/system/dns/host-entries/host-entry"

        def pre_process_list(self) -> None:
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.delete(
                        ["system", "static-host-mapping", "host-name"],
                        str(element.value["hostname"]),
                    )

        def pre_process(self) -> None:
            if self.replace:
                self.result.delete(
                    ["system", "static-host-mapping", "host-name"], self.key
                )

    def hostname(self, value: str) -> None:
        self.yy.result.pre_path = ["system", "static-host-mapping", "host-name", value]

    config = HostEntryConfig


class HostEntries(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:/system/dns/host-entries"

    host_entry = HostEntry


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
                    self.result.delete(
                        ["system", "name-server"], str(element.value["address"])
                    )

        def pre_process(self) -> None:
            if self.replace:
                self.result.delete(["system", "name-server"], self.key)

    def address(self, value: str) -> None:
        return self.yy.result.set(["system", "name-server"], value)

    config = DnsServerConfig


class DnsServers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers"

    server = DnsServer


class DnsConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/config"

        def pre_process(self) -> None:
            if self.replace:
                self.result.delete(["system", "domain-search"], "")

    def search(self, value: List[str]) -> None:
        for domain in value:
            self.yy.result.set(["system", "domain-search", "domain"], domain)


class Dns(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns"

    config = DnsConfig
    servers = DnsServers
    host_entries = HostEntries


class ClockConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock/config"

    def timezone_name(self, value: str) -> None:
        self.yy.result.set(["system", "time-zone"], value)


class Clock(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock"

    config = ClockConfig


class SystemConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/config"

    def hostname(self, value: str) -> None:
        self.yy.result.set(["system", "host-name"], value)

    def domain_name(self, value: str) -> None:
        self.yy.result.set(["system", "domain-name"], value)

    def login_banner(self, value: str) -> None:
        self.yy.result.set(["system", "login", "banner", "pre-login"], value)

    def motd_banner(self, value: str) -> None:
        self.yy.result.set(["system", "login", "banner", "post-login"], value)


class System(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system"

    config = SystemConfig
    clock = Clock
    dns = Dns
    ntp = Ntp
    ssh_server = SshServer
    logging = Logging
    aaa = Aaa
