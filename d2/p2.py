#!/usr/bin/env python3

import re


line_regex = re.compile(r"^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pw>.*)$")

valid_states = {(True, False), (False, True)}

if __name__ == "__main__":
    valid = 0
    with open("input", "r") as fh:
        for line in fh.readlines():
            match = line_regex.match(line.strip())
            assert match is not None, f"line {line} does not match!"

            pw = match.group("pw")
            min_cnt = int(match.group("min")) - 1
            max_cnt = int(match.group("max")) - 1
            lttr = match.group("char")

            if (pw[min_cnt] == lttr, pw[max_cnt] == lttr) in valid_states:
                valid += 1

    print(valid)
