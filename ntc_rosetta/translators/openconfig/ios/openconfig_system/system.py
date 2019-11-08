from yangify.translator import Translator, TranslatorData


class DnsConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/config"


class DnsServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server/config"


class DnsServer(Translator):
    config = DnsServerConfig

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(f"no dns server {element['address']}")

    def address(self, value: str):
        if value:
            self.yy.result.add_command(f"dns server {value}")


class DnsServers(Translator):
    server = DnsServer

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers"

        def pre_process(self) -> None:
            pass


class Dns(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns"

    config = DnsConfig
    servers = DnsServers


class NtpServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server/config"


class NtpServer(Translator):
    config = NtpServerConfig

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers/server"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(f"no ntp server {element['address']}")

    def address(self, value: str):
        self.yy.result.add_command(f"ntp server {value} prefer")


class NtpServers(Translator):
    server = NtpServer

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers"


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
        path = "/openconfig-system:system/ssh-server"

    config = SshServerConfig


class AaaAuthenticationUserConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user/config"

        def pre_process(self) -> None:
            self.extra = {
                "username": "",
                "password": "",
                "password_hash": "",
                "role": "",
                "ssh_key": "",
            }

        def post_process(self) -> None:
            extra = self.extra
            if not extra["username"] or not extra["role"] or not extra["password_hash"]:
                return None
            self.result.add_command(
                "username {} privilege {} secret {}".format(
                    extra["username"], extra["role"], extra["password_hash"]
                )
            )

    def username(self, value: str):
        self.yy.extra["username"] = value
        return None

    def role(self, value: str):
        self.yy.extra["role"] = value
        return None

    def password(self, value: str):
        self.yy.extra["password"] = value
        return None

    def password_hashed(self, value: str):
        self.yy.extra["password_hash"] = value
        return None

    def ssh_key(self, value: str):
        self.yy.extra["ssh_key"] = value
        return None


class AaaAuthenticationUser(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

    config = AaaAuthenticationUserConfig


class AaaAuthenticationUsers(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users"

    user = AaaAuthenticationUser


class AaaAuthentication(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication"

    users = AaaAuthenticationUsers


class Aaa(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa"

    authentication = AaaAuthentication


class SystemConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/config"

    def hostname(self, value: str) -> None:
        if value:
            self.yy.result.add_command(f"hostname {value}")
        else:
            self.yy.result.add_command(f"no hostname")


class System(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system"

        def pre_process(self) -> None:
            pass

    config = SystemConfig
    ssh_server = SshServer
    aaa = Aaa
    ntp = Ntp
    dns = Dns
