import json
from typing import List, Dict, Any


class RequestList:
    def __init__(self) -> None:
        self.requests: List[Dict[str, Any]] = []
        self.pre_path: List[str] = []

    def set(self, path: List[str], value: str, use_pre_path: bool = False) -> None:
        if use_pre_path:
            path = self.pre_path + path
        self.requests.append({"op": "set", "path": path, "value": value})

    def delete(self, path: List[str], value: str, use_pre_path: bool = False) -> None:
        if use_pre_path:
            path = self.pre_path + path
        self.requests.append({"op": "delete", "path": path, "value": value})

    # This is in preparation for possible move to using HTTP/API instead SSH for commands
    def to_json(self) -> str:
        return json.dumps(self.requests, indent=2)

    def to_set(self) -> str:
        result = ''
        for request in self.requests:
            result += f'{request["op"]} {" ".join(request["path"])} \'{request["value"]}\'\n'
        return result
