#!/usr/bin/env python3
import fileinput
import hashlib


def solve(data, zeroes):
    idx = 0
    target = "0" * zeroes
    while (
        not hashlib.md5(f"{data}{idx}".encode("utf-8")).hexdigest().startswith(target)
    ):
        idx += 1
    return idx


def main():
    data = fileinput.input().readline().rstrip()
    print(solve(data, 5))
    print(solve(data, 6))


main()
