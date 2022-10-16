#!/usr/bin/env python3
import fileinput
from itertools import groupby


def encode(s):
    encoded = [(char, len(list(group))) for char, group in groupby(list(s))]
    return "".join(f"{l}{c}" for (c, l) in encoded)


def solve(data, n):
    for _ in range(n):
        data = encode(data)
    return data


def main():
    data = fileinput.input().readline().rstrip()
    print(len(solve(data, 40)))
    print(len(solve(data, 50)))


main()
