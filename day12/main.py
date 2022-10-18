#!/usr/bin/env python3
import fileinput
import json


def solve(obj, ignore=None):
    def _solve(obj):
        match obj:
            case int():
                return obj
            case list():
                return sum(map(_solve, obj))
            case dict() if ignore not in obj.values():
                return sum(map(_solve, obj.values()))
            case _:
                return 0

    return _solve(obj)


def main():
    data = json.loads("".join(line for line in fileinput.input()))
    print(solve(data))
    print(solve(data, ignore="red"))


main()
