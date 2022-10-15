#!/usr/bin/env python3
import fileinput
from itertools import permutations


def solve(conns, f):
    locations = set(start for (start, _) in conns.keys())
    ways = permutations(locations)

    calculate = lambda locs: sum(
        conns[(start, end)] for (start, end) in zip(locs[:-1], locs[1:])
    )
    costs = list(map(calculate, ways))

    return f(costs)


def _parse(line):
    route, cost = line.split(" = ")
    start, end = route.split(" to ")
    return (start, end), int(cost)


def main():
    data = [_parse(line.rstrip()) for line in fileinput.input()]
    oneway = {conn: cost for conn, cost in data}
    connections = {
        **oneway,
        **{tuple(reversed(conn)): cost for (conn, cost) in oneway.items()},
    }
    print(solve(connections, f=min))
    print(solve(connections, f=max))


main()
