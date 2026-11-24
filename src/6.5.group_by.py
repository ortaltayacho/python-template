"""Group iterable elements by the result of a function."""

from collections.abc import Callable, Iterable
from typing import Any


def group_by(func: Callable[[Any], Any],
             iterable: Iterable[Any]) -> dict[Any, list[Any]]:
    """Group items by the value returned from applying func."""
    result = {}

    for item in iterable:
        key = func(item)

        if key not in result:
            result[key] = []

        result[key].append(item)

    return result


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))