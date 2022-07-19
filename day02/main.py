#!/usr/bin/env python3
import fileinput
from functools import reduce
from operator import mul


def paper(l, w, h):
    sides = (l * w, w * h, h * l)
    return 2 * sum(sides) + min(sides)


def part1(data):
    return sum(paper(*entry) for entry in data)


def part2(data):
    return sum(reduce(mul, entry, 1) + 2 * sum(entry[:2]) for entry in data)


def main():
    data = [
        tuple(sorted(map(int, line.rstrip().split("x")))) for line in fileinput.input()
    ]
    print(part1(data))
    print(part2(data))


main()
