#!/usr/bin/env python3

import re
from collections import Counter


line_regex = re.compile(r"^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pw>.*)$")


if __name__ == "__main__":
    valid = 0
    with open("input", "r") as fh:
        for line in fh.readlines():
            match = line_regex.match(line.strip())
            assert match is not None, f"line {line} does not match!"

            cnt = Counter(match.group("pw"))
            min_cnt = int(match.group("min"))
            max_cnt = int(match.group("max"))
            lttr = match.group("char")

            if min_cnt <= cnt[lttr] <= max_cnt:
                valid += 1

    print(valid)
