#!/usr/bin/env python

import copy


def print_floor(data):
    print("\n".join("".join(line) for line in data))
    print()


_coeff = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]


def occupied(data, pos_x, pos_y):
    cnt = 0

    for dir_x, dir_y in _coeff:
        cur_x = pos_x + dir_x
        cur_y = pos_y + dir_y

        while 0 <= cur_x < len(data[-1]) and 0 <= cur_y < len(data):
            if data[cur_y][cur_x] == "L":
                break

            if data[cur_y][cur_x] == "#":
                cnt += 1
                break

            cur_x = cur_x + dir_x
            cur_y = cur_y + dir_y

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
        if new_data[y][x] == "#" and occupied(new_data, x, y) > 4:
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
