#!/usr/bin/env python3
import fileinput
from collections import Counter


def add(t1, t2):
    (x1, y1), (x2, y2) = t1, t2
    return (x1 + x2, y1 + y2)


def solve(data, robo):
    size = 2 if robo else 1
    houses = [(0, 0) for _ in range(size)]
    move = lambda x, y: houses.append(add(houses[-size], (x, y)))
    for dir in data:
        if dir == "^":
            move(0, 1)
        elif dir == "v":
            move(0, -1)
        elif dir == ">":
            move(1, 0)
        elif dir == "<":
            move(-1, 0)
    return len(set(houses))


def main():
    data = fileinput.input().readline().rstrip()
    print(solve(data, False))
    print(solve(data, True))


main()
