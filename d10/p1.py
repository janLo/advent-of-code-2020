#!/usr/bin/env python3


if __name__ == "__main__":
    with open("input", "r") as fn:
        data = [0] + list(sorted(int(line.strip()) for line in fn))
        data.append(data[-1] + 3)

    counts = {1: 0, 2: 0, 3: 0}
    for pos in range(len(data) - 1):
        diff = data[pos + 1] - data[pos]
        assert 0 < diff < 4

        counts[diff] += 1

    print(counts[1] * counts[3])
