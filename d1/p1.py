#!/usr/bin/env python3

if __name__ == "__main__":
    with open("input", "r") as f:
        data = set([int(l.strip()) for l in f.readlines()])

    for item in data:
        if (2020 - item) in data:
            print(item, 2020 - item, item * (2020 - item))
            break
