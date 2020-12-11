#!/usr/bin/env python3


if __name__ == "__main__":
    with open("input", "r") as fn:
        data = [0] + list(sorted(int(line.strip()) for line in fn))
        data.append(data[-1] + 3)
    data.reverse()

    track = [1]
    for pos in range(1, len(data)):
        cur = data[pos]
        back_slice = data[pos - min(pos, 3) : pos]
        sm = sum(1 for x in back_slice if x - cur < 4 and pos > 0)
        track.append(sum(track[-sm:]))

        print(cur, sm, track)

    print(track[-1])
