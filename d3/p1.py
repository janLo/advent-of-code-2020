#!/usr/bin/env python3


def is_tree(line, pos):
    return line[pos % len(line)] == "#"


if __name__ == "__main__":

    shift = 3
    pos = 0
    trees = 0

    with open("input", "r") as fn:

        for line in fn:
            line = line.strip()

            if is_tree(line, pos):
                trees += 1

            pos = pos + shift

    print(trees)
