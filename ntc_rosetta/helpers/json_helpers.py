from typing import Any, Dict, Optional

import jmespath


def query(
    query: str,
    data: Dict[str, Any],
    force_list: bool = False,
    default: Optional[Any] = None,
) -> Any:
    """
    Query a nested dictionary using `jmespath <http://jmespath.org>`

    Args:
        query: jmespath query
        data: data to query
        force_list: return a list even if the object is not a list
        default: return this if the query returns None
    """
    res = jmespath.search(query, data)
    if res is None and force_list:
        return []
    if not isinstance(res, list) and force_list:
        return [res]
    return res if res is not None else default
