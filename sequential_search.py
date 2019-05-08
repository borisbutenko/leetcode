from typing import Iterable, Any


def ss(lst: Iterable[Any],
       search: Any) -> bool:
    found = False

    for item in lst:
        if item is search:
            found = True
            break

    return found
