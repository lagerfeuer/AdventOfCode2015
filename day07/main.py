#!/usr/bin/env python3.10
import fileinput
from functools import cache


def connect(left, gate, right):
    match gate:
        case "AND":
            return left & right
        case "OR":
            return left | right
        case "LSHIFT":
            return left << right
        case "RSHIFT":
            return left >> right


def solve(ops, target_wire):
    circuit = {}

    def resolve(w):
        try:
            return int(w)
        except ValueError:
            return _solve(w)

    @cache
    def _solve(wire):
        if wire not in circuit:
            op = ops[wire]
            result = None
            if len(op) == 1:
                result = resolve(op[0])
            elif len(op) == 2:
                _, wire_in = op
                result = ~resolve(wire_in) & 0xFFFF
            elif len(op) == 3:
                left, gate, right = op
                left, right = resolve(left), resolve(right)
                result = connect(left, gate, right)
            circuit[wire] = result

        return circuit[wire]

    return _solve(target_wire)


def _parse(line):
    tmp, out = line.split(" -> ")
    return tuple(tmp.strip().split(" ")), out


def main():
    gates = {
        out: op for (op, out) in [_parse(line.rstrip()) for line in fileinput.input()]
    }
    part1 = solve(gates, "a")
    print(part1)
    gates["b"] = (part1,)
    print(solve(gates, "a"))


main()
