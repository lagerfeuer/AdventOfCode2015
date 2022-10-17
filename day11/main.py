#!/usr/bin/env python3
import fileinput


def valid(pw):
    double = set()
    incr = set()

    if any(c in pw for c in "iol"):
        return False

    for (l, r) in zip(pw, pw[1:]):
        if l == r:
            double.add((l, r))
    if len(double) < 2:
        return False

    for (c1, c2, c3) in zip(pw, pw[1:], pw[2:]):
        if ord(c1) + 2 == ord(c2) + 1 == ord(c3):
            incr.add((c1, c2, c3))
    if len(incr) == 0:
        return False

    return True


def pwgen(pw):
    newpw = list(pw)
    init = True
    while not valid(newpw) or init:
        init = False
        idx = len(newpw) - 1
        incr = True
        while incr:
            if newpw[idx] != "z":
                newpw[idx] = chr(ord(newpw[idx]) + 1)
                incr = False
            else:
                newpw[idx] = "a"
                idx -= 1
    return "".join(newpw)


def solve(data):
    return pwgen(data)


def main():
    pw = fileinput.input().readline().rstrip()
    pw = solve(pw)
    print(pw)
    pw = solve(pw)
    print(pw)


main()
