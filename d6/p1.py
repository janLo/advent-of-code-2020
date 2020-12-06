#!/usr/bin/env python3

if __name__ == "__main__":
    groups = []
    with open("input", "r") as fn:

        group = set()
        for line in fn:
            line = line.strip()
            if len(line) == 0:
                groups.append(group)
                group = set()
                continue

            group.update(line)

        if len(line) != 0:
            groups.append(group)

    print(sum(len(g) for g in groups))
