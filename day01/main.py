#!/usr/bin/env python3
import fileinput
from functools import reduce
from itertools import accumulate

def wrap(data):
    return list(map(lambda e: 1 if e == '(' else -1, data))
    

def part1(data):
    return reduce(lambda acc, curr: acc + curr, wrap(data), 0)

def part2(data):
    return list(accumulate(wrap(data))).index(-1) + 1
    

def main():
    data = fileinput.input().readline()
    print(part1(data))
    print(part2(data))


main()
