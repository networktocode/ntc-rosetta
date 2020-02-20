import re

from yangify.translator import Translator, TranslatorData

from yangson.exceptions import InstanceValueError


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
                    self.result.add_command(f"no ip name-server {element['address']}")

    def address(self, value: str):
        self.yy.result.add_command(f"ip name-server {value}")


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
        self.yy.result.add_command(f"ntp server {value}")


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
            if not self.extra.get("username"):
                return
            role = self.extra.get("role")
            role_str = f" privilege {role}" if role else ""
            password = self.extra.get("password")
            password_str = f"password 0 {password}" if password else ""
            password_hash = self.extra.get("password_hash")
            match = re.match(r"^\$(\d).*", password_hash)
            password_hash_str = ""
            if match:
                hash_type = match.groups()[0]
                password_hash_str = f"secret {hash_type} {password_hash}"
            ssh_key = self.extra.get("ssh_key")
            ssh_key_str = f"ssh_key {ssh_key}" if ssh_key else ""  # noqa
            self.result.add_command(
                f"username {self.extra['username']}{role_str} {password_str or password_hash_str}"
            )
            # TODO: implement ssh_key
            # if ssh_key:
            #     """
            #     ip ssh pubkey-chain
            #       username test
            #         key-string
            #           some-rsa-ssh-key-string
            #         exit
            #       exit
            #     """
            #     raise NotImplementedError

    def username(self, value: str) -> None:
        self.yy.extra["username"] = value

    def role(self, value: str) -> None:
        self.yy.extra["role"] = value

    def password(self, value: str) -> None:
        self.yy.extra["password"] = value

    def password_hashed(self, value: str) -> None:
        self.yy.extra["password_hash"] = value

    def ssh_key(self, value: str) -> None:
        self.yy.extra["ssh_key"] = value


class AaaAuthenticationUser(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/aaa/authentication/users/user"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(f"no username {element['username']}")

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
        self.yy.result.add_command(f"hostname {value}")


class System(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system"

        def pre_process(self):
            if self.replace:
                raise InstanceValueError(
                    self.path, "Replace is not a supported operation for this path"
                )

    config = SystemConfig
    ssh_server = SshServer
    aaa = Aaa
    ntp = Ntp
    dns = Dns
