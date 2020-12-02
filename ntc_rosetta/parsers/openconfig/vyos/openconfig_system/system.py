from ipaddress import ip_address, IPv4Address, IPv6Address
from typing import Dict, Any, Optional, List, Iterator, Tuple

from yangify.parser import Parser, ParserData

from ntc_rosetta.helpers.vyos import SYSLOG_FACILITY, SYSLOG_SEVERITY


class AaaAuthenticationUserConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users/user/config"

    def username(self) -> str:
        return str(self.yy.key)

    def role(self) -> Optional[str]:
        return "openconfig-aaa:SYSTEM_ROLE_ADMIN"

    def password(self) -> Optional[str]:
        authentication = self.yy.native.get("authentication")
        if authentication:
            return authentication.get("plaintext-password")

    def password_hashed(self) -> Optional[str]:
        authentication = self.yy.native.get("authentication")
        if authentication:
            return authentication.get("encrypted-password")

    def ssh_key(self) -> Optional[str]:
        authentication = self.yy.native.get("authentication")
        if authentication and "public-keys" in authentication:
            for v in authentication.get("public-keys").values():
                # only return the first key
                return v["key"]


class AaaAuthenticationUser(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for k, v in self.native.get("user").items():
                yield k, v

    def username(self) -> str:
        return str(self.yy.key)

    config = AaaAuthenticationUserConfig


class AaaAuthenticationUsers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users"

    user = AaaAuthenticationUser


class AaaAuthenticationConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/config"

    def authentication_method(self) -> List[str]:
        return ["openconfig-aaa:RADIUS_ALL", "openconfig-aaa:LOCAL"]


class AaaAuthentication(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication"

    config = AaaAuthenticationConfig
    users = AaaAuthenticationUsers


class AaaRadiusConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/radius/config"

    def auth_port(self) -> Optional[int]:
        port = self.yy.native.get("port")
        if port:
            return int(port)

    def secret_key(self) -> Optional[str]:
        return self.yy.native.get("key")

    def source_address(self) -> Optional[str]:
        return (
            self.yy.root_native["dev_conf"]
            .get("system")
            .get("login")
            .get("radius")
            .get("source-address")
        )


class AaaRadius(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/radius"

    config = AaaRadiusConfig


class AaaServerGroupServersServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/config"

    def address(self) -> str:
        return self.yy.key


class AaaServerGroupServersServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            if self.native and "server" in self.native:
                for k, v in self.native["server"].items():
                    yield k, v

    def address(self) -> str:
        return self.yy.key

    radius = AaaRadius
    config = AaaServerGroupServersServerConfig


class AaaServerGroupServers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers"

    server = AaaServerGroupServersServer


class AaaServerGroupConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/config"

        def pre_process(self) -> None:
            self.native = (
                self.root_native["dev_conf"].get("system").get("login").get("radius")
            )

    def name(self) -> str:
        return self.yy.key

    def type(self):
        return "openconfig-aaa:RADIUS"


class AaaServerGroup(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            if self.native and "server" in self.native:
                yield "radius", self.native.get("radius")

    def name(self) -> str:
        # Reference to configured name of the server group
        return self.yy.key

    servers = AaaServerGroupServers
    config = AaaServerGroupConfig


class AaaServerGroups(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups"

    server_group = AaaServerGroup


class AaaAuthorizationConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authorization/config"

    def authorization_method(self) -> List[str]:
        return ["openconfig-aaa:RADIUS_ALL", "openconfig-aaa:LOCAL"]


class AaaAuthorization(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authorization"

    config = AaaAuthorizationConfig


class Aaa(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system").get("login")

    authentication = AaaAuthentication
    authorization = AaaAuthorization
    server_groups = AaaServerGroups


class SshServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ssh-server/config"

    def enable(self) -> bool:
        return "ssh" in self.yy.native

    def timeout(self) -> Optional[int]:
        return None

    def rate_limit(self) -> Optional[int]:
        return None

    def session_limit(self) -> Optional[int]:
        return None


class SshServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ssh-server"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("service")

    config = SshServerConfig


class NtpConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/config"

    def enabled(self) -> bool:
        return "ntp" in self.yy.native


class NtpServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers/server/config"

    def address(self) -> str:
        return str(self.yy.key)

    def prefer(self) -> Optional[bool]:
        return "prefer" in self.yy.native


class NtpServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            ntp = self.native.get("ntp")
            if ntp:
                for k, v in ntp.get("server").items():
                    yield k, v

    def address(self) -> str:
        return str(self.yy.key)

    config = NtpServerConfig


class NtpServers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers"

    server = NtpServer


class Ntp(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system")

    config = NtpConfig
    servers = NtpServers


class DnsServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers/server/config"

    def address(self) -> str:
        return str(self.yy.key)

    def port(self) -> int:
        return 53


class DnsServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            if self.native.get("name-server"):
                for i in self.native["name-server"]:
                    yield i, i

    def address(self) -> str:
        return str(self.yy.key)

    config = DnsServerConfig


class DnsServers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers"

    server = DnsServer


class DnsConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/config"

    def search(self) -> Optional[List[str]]:
        domain_search = self.yy.native.get("domain-search")
        if domain_search:
            return domain_search.get("domain")


class HostEntryConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:/system/dns/host-entries/host-entry/config"

    def hostname(self) -> str:
        return self.yy.key

    def alias(self) -> Optional[List[str]]:
        return [self.yy.native.get("alias")]

    def ipv4_address(self) -> Optional[List[str]]:
        inet = self.yy.native["inet"]
        try:
            if type(ip_address(inet)) is IPv4Address:
                return [inet]
        except ValueError:
            raise Exception(f"address is not valid IPv4 for host entry {self.yy.key}")

    def ipv6_address(self) -> Optional[List[str]]:
        inet = self.yy.native["inet"]
        try:
            if type(ip_address(inet)) is IPv6Address:
                return [inet]
        except ValueError:
            raise Exception(f"address is not valid IPv6 for host entry {self.yy.key}")


class HostEntry(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:/system/dns/host-entries/host-entry"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            static_host_mapping = self.native.get("static-host-mapping")
            if static_host_mapping:
                for k, v in static_host_mapping.get("host-name").items():
                    yield k, v

    def hostname(self) -> str:
        return str(self.yy.key)

    config = HostEntryConfig


class HostEntries(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:/system/dns/host-entries"

    host_entry = HostEntry


class Dns(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system")

    config = DnsConfig
    servers = DnsServers
    host_entries = HostEntries


class ClockConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/clock/config"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system")

    def timezone_name(self) -> str:
        return self.yy.native.get("time-zone")


class Clock(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/clock"

    config = ClockConfig


class SystemConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/config"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system")

    def hostname(self) -> Optional[str]:
        return self.yy.native.get("host-name")

    def domain_name(self) -> Optional[str]:
        return self.yy.native.get("domain-name")

    def login_banner(self) -> Optional[str]:
        banner = self.yy.native.get("login").get("banner")
        if banner:
            return banner.get("pre-login")

    def motd_banner(self) -> Optional[str]:
        banner = self.yy.native.get("login").get("banner")
        if banner:
            return banner.get("post-login")


class ConsoleSelectorConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/console/selectors/selector/config"

    def facility(self) -> str:
        return SYSLOG_FACILITY[self.yy.key]

    def severity(self) -> str:
        return SYSLOG_SEVERITY[self.yy.native["level"]]


class ConsoleSelector(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/console/selectors/selector"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            if self.native and "facility" in self.native:
                for k, v in self.native["facility"].items():
                    if SYSLOG_FACILITY[k]:
                        yield k, v

    def facility(self) -> str:
        return SYSLOG_FACILITY[self.yy.key]

    def severity(self) -> str:
        return SYSLOG_SEVERITY[self.yy.native["level"]]

    config = ConsoleSelectorConfig


class ConsoleSelectors(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/console/selectors"

    selector = ConsoleSelector


class Console(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/console"

        def pre_process(self) -> None:
            self.native = (
                self.root_native["dev_conf"].get("system").get("syslog").get("console")
            )

    selectors = ConsoleSelectors


class RemoteServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/remote-servers/remote-server/config"

    def host(self) -> str:
        return self.yy.key

    def remote_port(self) -> Optional[int]:
        return int(self.yy.native.get("port", 514))


class RemoteServerSelectorConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/remote-servers/remote-server/selectors/selector/config"

    def facility(self) -> str:
        return SYSLOG_FACILITY[self.yy.key]

    def severity(self) -> str:
        return SYSLOG_SEVERITY[self.yy.native["level"]]


class RemoteServerSelector(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/remote-servers/remote-server/selectors/selector"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            if self.native and "facility" in self.native:
                for k, v in self.native["facility"].items():
                    if SYSLOG_FACILITY[k]:
                        yield k, v

    def facility(self) -> str:
        return SYSLOG_FACILITY[self.yy.key]

    def severity(self) -> str:
        return SYSLOG_SEVERITY[self.yy.native["level"]]

    config = RemoteServerSelectorConfig


class RemoteServerSelectors(Parser):
    class Yangify(ParserData):
        path = (
            "/openconfig-system:system/logging/remote-servers/remote-server/selectors"
        )

    selector = RemoteServerSelector


class RemoteServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/remote-servers/remote-server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            hosts = self.native.get("syslog").get("host")
            if hosts:
                for k, v in hosts.items():
                    yield k, v

    def host(self) -> str:
        return self.yy.key

    config = RemoteServerConfig
    selectors = RemoteServerSelectors


class RemoteServers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging/remote-servers"

    remote_server = RemoteServer


class Logging(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/logging"

        def pre_process(self) -> None:
            self.native = self.root_native["dev_conf"].get("system")

    console = Console
    remote_servers = RemoteServers


class System(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system"

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]

    config = SystemConfig
    clock = Clock
    dns = Dns
    ntp = Ntp
    ssh_server = SshServer
    logging = Logging
    aaa = Aaa
