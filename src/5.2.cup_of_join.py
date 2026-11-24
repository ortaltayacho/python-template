"""Join multiple lists into one list with a separator."""


def join(*args: list, sep: str = "-") -> list | None:
    """Combine lists, inserting a separator between consecutive lists."""

    if not args:
        return None

    res = []

    for i, current_list in enumerate(args):
        res.extend(current_list)

        if i < len(args) - 1:
            res.append(sep)

    return res


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep="@"))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
