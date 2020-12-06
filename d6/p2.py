#!/usr/bin/env python3

if __name__ == "__main__":
    groups = []
    with open("input", "r") as fn:

        group = None
        for line in fn:
            line = line.strip()
            if len(line) == 0:
                groups.append(group)
                group = None
                continue

            if group is None:
                group = set(line)
            else:
                group = group.intersection(set(line))

        if len(line) != 0:
            groups.append(group)

    print(sum(len(g) for g in groups))
