#!/usr/bin/env python

import copy


def print_floor(data):
    print("\n".join("".join(line) for line in data))
    print()


def occupied(data, pos_x, pos_y):
    min_x = max(0, pos_x - 1)
    min_y = max(0, pos_y - 1)

    max_x = min(len(data[-1]), pos_x + 2)
    max_y = min(len(data), pos_y + 2)

    cnt = 0
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if not (x == pos_x and y == pos_y) and data[y][x] == "#":
                cnt += 1

    return cnt


def iter_full(data):
    for y in range(len(data)):
        for x in range(len(data[-1])):
            yield y, x


def fill(data):
    new_data = copy.deepcopy(data)

    cnt = 0
    for y, x in iter_full(data):
        if new_data[y][x] == "L" and occupied(new_data, x, y) == 0:
            data[y][x] = "#"
            cnt += 1

    return cnt


def clean(data):
    new_data = copy.deepcopy(data)

    cnt = 0
    for y, x in iter_full(data):
        if new_data[y][x] == "#" and occupied(new_data, x, y) > 3:
            data[y][x] = "L"
            cnt += 1

    return cnt


if __name__ == "__main__":
    with open("input", "r") as fn:
        data = [[pos for pos in line.strip()] for line in fn]

    changes = [1]

    while sum(changes[-2:]) > 0:
        changes.append(fill(data))
        print_floor(data)

        changes.append(clean(data))
        print_floor(data)

    print(sum(1 for y, x in iter_full(data) if data[y][x] == "#"))
