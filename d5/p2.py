#!/usr/bin/env python3


_fac = {"F": 0, "B": 1, "L": 0, "R": 1}


def get_pos(spec, items_cnt):
    half = items_cnt / 2
    space = [x for x in range(items_cnt)]

    for partition in spec:
        half = int(len(space) / 2)
        start = half * _fac[partition]
        end = half * (_fac[partition] + 1)

        space = space[start:end]

    assert len(space) == 1, "not enough partitions"
    return space[0]


if __name__ == "__main__":
    all_seats = set(range((127 * 8) + 7))
    occupied_seats = set()

    with open("input", "r") as fh:
        for line in fh:
            line = line.strip()

            seat_row = get_pos(line[:7], 128)
            seat_col = get_pos(line[7:], 8)
            seat_id = (seat_row * 8) + seat_col
            occupied_seats.add(seat_id)

    free = all_seats - occupied_seats
    for seat_id in free:
        if (seat_id - 1) in occupied_seats and (seat_id + 1) in occupied_seats:
            print(seat_id)
