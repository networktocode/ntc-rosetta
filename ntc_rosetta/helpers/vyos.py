"""VyOS helper consts and methods"""
from typing import Dict, Any, List

SYSLOG_FACILITY = {
    "all": "ALL",
    "auth": "AUTH",
    "authpriv": "AUTHPRIV",
    "cron": None,
    "daemon": "SYSTEM_DAEMON",
    "kern": "KERNEL",
    "lpr": None,
    "mail": "MAIL",
    "mark": None,
    "news": None,
    "protocols": "LOCAL7",
    "security": "AUTH",
    "syslog": "SYSLOG",
    "user": "USER",
    "uucp": None,
    "local0": "LOCAL0",
    "local1": "LOCAL1",
    "local2": "LOCAL2",
    "local3": "LOCAL3",
    "local4": "LOCAL4",
    "local5": "LOCAL5",
    "local6": "LOCAL6",
    "local7": "LOCAL7",
}
SYSLOG_SEVERITY = {
    "emerg": "EMERGENCY",
    "alert": "ALERT",
    "crit": "CRITICAL",
    "err": "ERROR",
    "warning": "WARNING",
    "notice": "NOTICE",
    "info": "INFORMATIONAL",
    "debug": "DEBUG",
    "all": "DEBUG",
}


def parse_config_tree(config: List[str]) -> Dict[str, Any]:
    parsed: Dict[str, Any] = {}
    while True:
        if not config:
            break
        line = config.pop(0).rstrip()
        if line.lstrip().startswith("/*"):
            continue
        nodes = line.lstrip().split()
        if nodes[-1] == "{":
            if len(nodes) > 2:
                parsed.setdefault(nodes[0], {}).update(
                    {nodes[1]: parse_config_tree(config)}
                )
            else:
                parsed[nodes[0]] = parse_config_tree(config)
        elif nodes[-1] == "}":
            break
        else:
            if len(nodes) == 1:
                parsed[nodes[0]] = ""
            else:
                if nodes[1].startswith('"'):
                    nodes[1] = nodes[1].lstrip('"')
                    nodes[-1] = nodes[-1].rstrip('"')
                    value = " ".join(nodes[1:])
                else:
                    value = str(nodes[1])
                if nodes[0] in parsed:
                    if isinstance(parsed[nodes[0]], list):
                        parsed[nodes[0]].append(value)
                    else:
                        parsed[nodes[0]] = [parsed[nodes[0]], value]
                else:
                    parsed[nodes[0]] = value
    return parsed
