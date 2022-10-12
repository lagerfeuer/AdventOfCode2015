#!/usr/bin/env python3
from curses.ascii import SI
import fileinput
import re
from collections import namedtuple

Command = namedtuple("Command", "instr start end")
Point = namedtuple("Point", "x y")

SIZE = 1000
REGEX = re.compile(
    r"(turn )?(?P<instr>on|off|toggle) (?P<start>\d+,\d+) through (?P<end>\d+,\d+)"
)
ACTIONS = {
    False: {"toggle": lambda x: (x + 1) % 2, "on": lambda _: 1, "off": lambda _: 0},
    True: {
        "toggle": lambda x: x + 2,
        "on": lambda x: x + 1,
        "off": lambda x: x - 1 if x else 0,
    },
}


def _parse(line):
    m = REGEX.match(line)
    start = map(int, m["start"].split(","))
    end = map(int, m["end"].split(","))
    return Command(m["instr"], Point(*start), Point(*end))


def solve(data, brightness_enabled):
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for cmd in data:
        rng = [
            (x, y)
            for x in range(cmd.start.x, cmd.end.x + 1)
            for y in range(cmd.start.y, cmd.end.y + 1)
        ]
        for (x, y) in rng:
            grid[x][y] = ACTIONS[brightness_enabled][cmd.instr](grid[x][y])
    flattened = [cell for row in grid for cell in row]
    return sum(flattened)


def main():
    data = [_parse(line.rstrip()) for line in fileinput.input()]
    print(solve(data, False))
    print(solve(data, True))


main()
