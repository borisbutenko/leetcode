from typing import Iterable, Any


def ss(lst: Iterable[Any],
       search: Any) -> bool:
    """Sequential search example

    :param lst: {Iterable[Any]}
    :param search: {Any}
    :return: {bool} is the search in list
    """
    found = False

    for item in lst:
        if item is search:
            found = True
            break

    return found
