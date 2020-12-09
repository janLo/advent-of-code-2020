#!/usr/bin/env python3


def check_valid(cur, prev):
    for item in prev:
        if cur > item:
            other = cur - item
            if other != item and other in prev:
                return item, other


if __name__ == "__main__":

    with open("input", "r") as fn:
        data = [int(item.strip()) for item in fn]

    for pos in range(25, len(data)):
        cur = data[pos]
        prev = data[pos - 25 : pos]

        res = check_valid(cur, prev)
        if res is None:
            print(cur)
            break
