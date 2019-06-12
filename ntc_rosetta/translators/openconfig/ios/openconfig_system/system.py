from yangify.translator import Translator, TranslatorData, unneeded
from ntc_rosetta.helpers import json_helpers as jh

import json

class DnsConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/dns/config"

class DnsServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/dns/servers/server/config"

class DnsServer(Translator):
    config = DnsServerConfig

    class Yangify(TranslatorData):
        path = "openconfig-system:system/dns/servers/server"

    address = unneeded

class DnsServers(Translator):
    server = DnsServer

    class Yangify(TranslatorData):
        path = "openconfig-system:system/dns/servers"

        def pre_process(self) -> None:
            pass

class Dns(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/dns"

    config = DnsConfig
    servers = DnsServers

class NtpConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/ntp"

class Ntp(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/ntp"

    config = NtpConfig

class SshServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/ssh-server/config"

    def protocol_version(self, value: str) -> None:
        if value == "V2":
            self.yy.result.add_command(f"ip ssh version 2")
        elif value == "V1":
            self.yy.result.add_command(f"ip ssh version 1")
        else:
            self.yy.result.add_command(f"default ip ssh version")

    def timeout(self, value: int) -> None:
        if value:
            self.yy.result.add_command(f"ip ssh time-out {value}")

class SshServer(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/ssh-server"

    config = SshServerConfig

class AaaAuthenticationUserConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/aaa/authentication/users/user/config"

    def username(self, value: str):
        print(value)
        print(jh.query('config', self.yy.candidate["openconfig-system:system"]))
        # print(self.yy.candidate['openconfig-system:system']['aaa'])
        # print(dir(self.yy.root_result))
        return None

class AaaAuthenticationUser(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/aaa/authentication/users/user"

    config = AaaAuthenticationUserConfig

class AaaAuthenticationUsers(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/aaa/authentication/users"

    user = AaaAuthenticationUser

class AaaAuthentication(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/aaa/authentication"

    users = AaaAuthenticationUsers

class Aaa(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/aaa"

    authentication = AaaAuthentication

class SystemConfig(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system/config"

    def hostname(self, value: str) -> None:
        if value:
            self.yy.result.add_command(f"hostname {value}")
        else:
            self.yy.result.add_command(f"no hostname")

class System(Translator):
    class Yangify(TranslatorData):
        path = "openconfig-system:system"

        def pre_process(self) -> None:
            pass

    config = SystemConfig
    ssh_server = SshServer
    aaa = Aaa
