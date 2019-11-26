from typing import Any, Dict, Iterator, Tuple, Optional

from yangify.parser import Parser, ParserData, unneeded


class ClockConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/clock/config"

    def timezone_name(self) -> str:
        tz = self.yy.native.xpath("/configuration/system/time-zone")
        if tz:
            return tz[0].text


class Clock(Parser):
    config = ClockConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/clock"


class DnsConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/config"

    search = unneeded


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
            for i in self.native.xpath("/configuration/system/name-server/name"):
                yield i.text, i

    def address(self) -> str:
        return str(self.yy.key)

    config = DnsServerConfig


class DnsServers(Parser):
    server = DnsServer

    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers"


class Dns(Parser):
    config = DnsConfig
    servers = DnsServers

    class Yangify(ParserData):
        path = "/openconfig-system:system/dns"


class NtpConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/config"

    def enabled(self) -> bool:
        True

    def ntp_source_address(self) -> Optional[str]:
        # TODO
        return None

    def enable_ntp_auth(self) -> Optional[bool]:
        # TODO
        return None


class NtpServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers/server/config"

    def address(self) -> str:
        return str(self.yy.key)


class NtpServer(Parser):
    config = NtpServerConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for i in self.native.xpath("/configuration/system/ntp/server"):
                server = i.xpath("name")
                if server:
                    yield server[0].text, i

    def address(self) -> str:
        return str(self.yy.key)


class NtpServers(Parser):
    server = NtpServer

    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp/servers"


class Ntp(Parser):
    config = NtpConfig
    servers = NtpServers

    class Yangify(ParserData):
        path = "/openconfig-system:system/ntp"


class SshServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/ssh-server/config"

    def enable(self) -> bool:
        # NOTE: This is always true
        return True

    def protocol_version(self) -> str:
        ssh = self.yy.native.xpath("/configuration/system/services/ssh")
        pv = None
        if ssh:
            pv = ssh[0].findtext("protocol-version")
        if pv and pv == "v2":
            return "V2"
        if pv and pv == "v1":
            return "V1"
        return "V1_V2"

    def timeout(self) -> Optional[int]:
        return None


class SshServer(Parser):
    config = SshServerConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/ssh-server"


class TelnetServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/telnet-server/config"

    def enable(self) -> bool:
        return False

    def timeout(self) -> Optional[int]:
        return None


class TelnetServer(Parser):
    config = TelnetServerConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/telnet-server"


class AaaAuthenticationUserConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users/user/config"

    def username(self) -> str:
        return str(self.yy.key)

    def role(self) -> Optional[str]:
        cls = self.yy.native.xpath("class")
        if cls:
            return cls[0].text

    def password(self) -> Optional[str]:
        elem = self.yy.native.xpath("authentication")
        if elem:
            password = elem[0].findtext("password")
            return password

    def password_hashed(self) -> Optional[str]:
        elem = self.yy.native.xpath("authentication")
        if elem:
            enc_pass = elem[0].findtext("encrypted-password")
            return enc_pass

    def ssh_key(self) -> Optional[str]:
        algs = ["ssh-ecdsa", "ssh-ed25519", "ssh-rsa"]
        for alg in algs:
            elem = self.yy.native.xpath(f"authentication/{alg}")
            if elem:
                key = elem[0].findtext("name")
                return key


class AaaAuthenticationUser(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for i in self.native.xpath("/configuration/system/login/user"):
                yield i.findtext("name"), i

    def username(self) -> str:
        return str(self.yy.key)

    config = AaaAuthenticationUserConfig


class AaaAuthenticationUsers(Parser):
    user = AaaAuthenticationUser

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users"


class AaaAuthentication(Parser):
    users = AaaAuthenticationUsers

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication"


class AaaTacacsConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/tacacs/config"

    def secret_key(self) -> Optional[str]:
        return self.yy.native.findtext("secret")

    def source_address(self) -> Optional[str]:
        # TODO
        pass

    def port(self) -> Optional[int]:
        # TODO
        pass


class AaaTacacs(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/tacacs"

    config = AaaTacacsConfig


class AaaServerGroupServersServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server/config"

    def address(self) -> str:
        return self.yy.key


class AaaServerGroupServersServer(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for i in self.native[0].xpath("tacplus-server"):
                yield i.findtext("name"), i

    def address(self) -> str:
        return self.yy.key

    tacacs = AaaTacacs
    config = AaaServerGroupServersServerConfig


class AaaServerGroupServers(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/servers"

    server = AaaServerGroupServersServer


class AaaServerGroupConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group/config"

    def name(self) -> str:
        return self.yy.key

    def type(self):
        return "openconfig-aaa:TACACS"


class AaaServerGroup(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups/server-group"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            yield "tacacs", self.native.xpath("/configuration/system")

    def name(self) -> str:
        # Reference to configured name of the server group
        return "tacacs"

    servers = AaaServerGroupServers
    config = AaaServerGroupConfig


class AaaServerGroups(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/server-groups"

    server_group = AaaServerGroup


class Aaa(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa"

    authentication = AaaAuthentication
    server_groups = AaaServerGroups


class SystemConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/config"

    def hostname(self) -> Optional[str]:
        hostname = self.yy.native.xpath("/system/host-name")
        if hostname:
            return hostname[0].text

    def domain_name(self) -> Optional[str]:
        domain = self.yy.native.xpath("/system/domain-name")
        if domain:
            return domain[0].text

    def login_banner(self) -> Optional[str]:
        announcement = self.yy.native.xpath("/system/login/announcement")
        if announcement:
            return announcement[0].text

    def motd_banner(self) -> Optional[str]:
        message = self.yy.native.xpath("/system/login/message")
        if message:
            return message[0].text


class System(Parser):
    config = SystemConfig
    clock = Clock
    dns = Dns
    ntp = Ntp
    ssh_server = SshServer
    telnet_server = TelnetServer
    aaa = Aaa

    class Yangify(ParserData):
        path = "/openconfig-system:system"

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]
