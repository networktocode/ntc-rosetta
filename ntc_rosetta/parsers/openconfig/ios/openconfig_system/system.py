from typing import Any, Dict, Iterator, Tuple

from ntc_rosetta.helpers import json_helpers as jh

from yangify.parser import Parser, ParserData


import re


class ClockConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/clock/config"

    def timezone_name(self) -> str:
        v = jh.query('clock.timezone."#text"', self.yy.native)
        if v is not None:
            return str(v)
        return None


class Clock(Parser):
    config = ClockConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/clock"


class DnsConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/config"

    def search(self) -> str:
        return None


class DnsServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers/server/config"

    def address(self) -> str:
        return str(self.yy.key)

    def port(self) -> int:
        return 53


class DnsServer(Parser):
    config = DnsServerConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/dns/servers/server"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            dns = jh.query('ip."name-server"."#text"', self.native) or ""
            for ns in dns.split(" "):
                yield ns, {}

    def address(self) -> str:
        return str(self.yy.key)


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
        if jh.query("ntp", self.yy.native):
            return True
        return False

    def ntp_source_address(self) -> str:
        return None

    def enable_ntp_auth(self) -> bool:
        if jh.query("ntp.authenticate", self.yy.native):
            return True
        return False


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
            ntp_servers = jh.query("ntp.server", self.native) or {}
            for k, v in ntp_servers.items():
                if k == "#text":
                    continue
                yield k, v

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
        version = jh.query('ip.ssh.version."#text"', self.yy.native)

        if version and version == "2":
            return "V2"
        elif version and version == "1":
            return "V1"
        return "V1_V2"

    def timeout(self) -> int:
        timeout = jh.query('ip.ssh."time-out"."#text"', self.yy.native)
        if timeout:
            return timeout
        return None


class SshServer(Parser):
    config = SshServerConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/ssh-server"


class TelnetServerConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/telnet-server/config"

    def enable(self) -> bool:
        # TODO: I believe this is always enabled, but need a way to check if it
        # is listening on the tty ports
        return True

    def timeout(self) -> int:
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

    def role(self) -> str:
        text = jh.query('"#text"', self.yy.native)

        role_RE = r"privilege\s(\d+)(?:\ssecret|\spassword)"
        result = re.match(role_RE, text)

        if result:
            return result[1]
        return None

    def password(self) -> str:
        text = jh.query('"#text"', self.yy.native)
        password_RE = r".*password ((\d) )?(.*)"
        result = re.match(password_RE, text)

        if result:
            _, _, password = result.groups()
            return password
        return None

    def password_hashed(self) -> str:
        text = jh.query('"#text"', self.yy.native)
        password_RE = r".*secret ((\d) )?(.*)"
        result = re.match(password_RE, text)

        if result:
            _, _, secret = result.groups()
            return secret
        return None

    def ssh_key(self) -> str:
        return None


class AaaAuthenticationUser(Parser):
    config = AaaAuthenticationUserConfig

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            users = jh.query("username", self.native) or {}
            for k, v in users.items():
                if k == "#text":
                    continue
                yield k, v

    def username(self) -> str:
        return str(self.yy.key)


class AaaAuthenticationUsers(Parser):
    user = AaaAuthenticationUser

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication/users"


class AaaAuthentication(Parser):
    users = AaaAuthenticationUsers

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa/authentication"


class Aaa(Parser):
    authentication = AaaAuthentication

    class Yangify(ParserData):
        path = "/openconfig-system:system/aaa"


class SystemConfig(Parser):
    class Yangify(ParserData):
        path = "/openconfig-system:system/config"

    def hostname(self) -> str:
        v = jh.query('hostname."#text"', self.yy.native)
        if v is not None:
            return str(v)
        else:
            return None

    def domain_name(self) -> str:
        v = jh.query('ip."domain-name"."#text"', self.yy.native)
        if v is not None:
            return str(v)
        else:
            return None

    def login_banner(self) -> str:
        # TODO
        return None

    def motd_banner(self) -> str:
        # TODO
        return None


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
        metadata = {"key": "dev_conf", "command": "show running-config all"}

        def pre_process(self) -> None:
            self.native: Dict[str, Any] = self.root_native["dev_conf"]
