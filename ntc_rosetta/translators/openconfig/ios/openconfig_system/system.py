import re

from ntc_rosetta.helpers.ios import HASH_MAP

from yangify.translator import Translator, TranslatorData

from yangson.exceptions import InstanceValueError, UnexpectedInput


class DnsConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/config"


class DnsServerConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server/config"

    def address(self, value: str):
        self.yy.extra["dns_servers"].append(value)


class DnsServer(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers/server"

        def pre_process_list(self) -> None:
            self.extra = {"dns_servers": []}
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(f"no ip name-server {element['address']}")

        def post_process_list(self):
            if self.extra["dns_servers"]:
                self.result.add_command(
                    f"ip name-server {' '.join(self.extra['dns_servers'])}"
                )

    config = DnsServerConfig


class DnsServers(Translator):
    server = DnsServer

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/dns/servers"


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

    def address(self, value: str) -> None:
        self.yy.result.add_command(f"ntp server {value}")


class NtpServers(Translator):
    server = NtpServer

    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/servers"


class NtpConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/config"

    def enable_ntp_auth(self, value: bool) -> None:
        if value:
            self.yy.result.add_command("ntp authenticate")


class NtpKeyConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/ntp-keys/ntp-key/config"

        def pre_process(self) -> None:
            self.extra = {"key-id": "", "key-type": "", "key-value": ""}

        def post_process(self) -> None:
            self.result.add_command(
                f"ntp authentication-key {self.extra['key-id']} "
                f"{self.extra['key-type']} {self.extra['key-value']}"
            )

    def key_id(self, value: str) -> None:
        self.yy.extra["key-id"] = value

    def key_type(self, value: str) -> None:
        # md5 is our only choice for now
        self.yy.extra["key-type"] = "md5"

    def key_value(self, value: str) -> None:
        self.yy.extra["key-value"] = value


class NtpKey(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/ntp-keys/ntp-key"

        def pre_process_list(self) -> None:
            if self.to_remove:
                for element in self.to_remove:
                    self.result.add_command(
                        f"no ntp authentication-key {element['key-id']}"
                    )

    config = NtpKeyConfig


class NtpKeys(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp/ntp-keys"

    ntp_key = NtpKey


class Ntp(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/ntp"

    config = NtpConfig
    servers = NtpServers
    ntp_keys = NtpKeys


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
                hash_type_str = match.groups()[0]
                hash_type = HASH_MAP.get(hash_type_str)
                if not hash_type:
                    raise UnexpectedInput("Unsupported hash type")
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


class ClockConfig(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock/config"

    def timezone_name(self, value: str) -> None:
        self.yy.result.add_command(f"clock timezone {value}")


class Clock(Translator):
    class Yangify(TranslatorData):
        path = "/openconfig-system:system/clock"

    config = ClockConfig


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
    clock = Clock
