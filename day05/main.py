#!/usr/bin/env python3
import fileinput
from collections import defaultdict

VOWELS = set(list("aeiou"))
FORBIDDEN = [tuple(e) for e in ["ab", "cd", "pq", "xy"]]


def is_nice_1(s):
    vowels = defaultdict(int)
    double = False
    for idx in range(len(s)):
        last, curr = None if idx == 0 else s[idx - 1], s[idx]
        if curr in VOWELS:
            vowels[curr] += 1
        if last == curr:
            double = True
        if (last, curr) in FORBIDDEN:
            return False

    return sum(vowels.values()) >= 3 and double


def is_nice_2(s):
    pos = defaultdict(list)
    for idx, pair in enumerate([s[idx : idx + 2] for idx in range(len(s) - 1)]):
        pos[pair].append(idx)

    two_pair = any(abs(max(l) - min(l) > 1) for l in pos.values())
    repeat = any(
        x == z for (x, _, z) in [s[idx : idx + 3] for idx in range(len(s) - 2)]
    )

    return two_pair and repeat


def solve(data, f):
    return [f(s) for s in data].count(True)


def main():
    data = [line.rstrip() for line in fileinput.input()]
    print(solve(data, is_nice_1))
    print(solve(data, is_nice_2))


main()
