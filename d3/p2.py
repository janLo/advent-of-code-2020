#!/usr/bin/env python3

import math


def is_tree(line, pos):
    return line[pos % len(line)] == "#"


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


if __name__ == "__main__":

    slope = -1
    all_trees = []

    for shift, step in slopes:
        slope += 1
        pos = 0
        row = -1
        trees = 0

        with open("input", "r") as fn:
            for line in fn:
                row += 1

                if row % step != 0:
                    continue

                line = line.strip()

                if is_tree(line, pos):
                    trees += 1

                pos = pos + shift

            all_trees.append(trees)

    print(math.prod(all_trees))
