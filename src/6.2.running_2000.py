"""Measure the execution time of a function."""

import time
from collections.abc import Callable
from typing import Any


def timer(f: Callable, *args: Any, **kwargs: Any) -> float:
    """Run a function and return its execution time in seconds."""
    start_time = time.perf_counter()

    f(*args, **kwargs)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return execution_time


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
