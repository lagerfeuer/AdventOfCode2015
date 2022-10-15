#!/usr/bin/env python3
import fileinput


def solve1(data):
    length = lambda line: len(line[1:-1].encode("ascii").decode("unicode_escape"))
    return sum(map(len, data)) - sum(map(length, data))


def solve2(data):
    length = lambda line: line.count("\\") + line.count('"') + len(line) + 2
    return sum(map(length, data)) - sum(map(len, data))


def main():
    data = [line.rstrip() for line in fileinput.input()]
    print(solve1(data))
    print(solve2(data))


main()
