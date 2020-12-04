#!/usr/bin/env python3

if __name__ == "__main__":
    with open("input", "r") as f:
        data = list([int(l.strip()) for l in f.readlines()])

    cnt = len(data)
    for pos1 in range(cnt):
        for pos2 in range(pos1 + 1, cnt):
            item1 = data[pos1]
            item2 = data[pos2]
            sums = item1 + item2

            if (2020 - sums) in data[pos2 + 1 :]:
                print(item1, item2, 2020 - sums, item1 * item2 * (2020 - sums))
                break
