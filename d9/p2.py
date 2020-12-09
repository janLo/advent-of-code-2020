#!/usr/bin/env python3


def check_valid(cur, prev):
    for item in prev:
        if cur > item:
            other = cur - item
            if other != item and other in prev:
                return item, other


def find_invalid(data):
    for pos in range(25, len(data)):
        cur = data[pos]
        prev = data[pos - 25 : pos]

        res = check_valid(cur, prev)
        if res is None:
            return cur


def find_sum_range(data, invalid):
    for start in range(len(data)):
        sumup = data[start]
        for end in range(start + 1, len(data)):
            sumup += data[end]

            if sumup == invalid:
                return start, end

            elif sumup > invalid:
                break


if __name__ == "__main__":

    with open("input", "r") as fn:
        data = [int(item.strip()) for item in fn]

    invalid = find_invalid(data)
    start, end = find_sum_range(data, invalid)
    sum_range = data[start : end + 1]

    print(min(sum_range) + max(sum_range))
