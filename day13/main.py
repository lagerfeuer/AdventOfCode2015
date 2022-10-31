#!/usr/bin/env python3
import fileinput
import re
from collections import defaultdict
from itertools import permutations


regex = re.compile(
    r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
)


def _parse(line):
    m = regex.match(line)
    return (m[1], m[4]), int(m[3]) if m[2] == "gain" else -int(m[3])


def solve(data, seat_self):
    people = set(data.keys())
    perms = permutations(people)
    results = {}
    for perm in perms:
        tmp = [
            data[perm[idx]][perm[(idx + 1) % len(perm)]]
            + data[perm[(idx + 1) % len(perm)]][perm[idx]]
            for idx in range(len(perm))
        ]
        results[perm] = tmp

    optimal = max(results.values(), key=lambda x: sum(x))
    if not seat_self:
        return sum(optimal)

    return sum(optimal) - min(optimal)


def main():
    parsed = [_parse(line.rstrip()) for line in fileinput.input()]
    hmap = defaultdict(dict)
    for (left, right), val in parsed:
        hmap[left][right] = val
    print(solve(hmap, False))
    print(solve(hmap, True))


main()
