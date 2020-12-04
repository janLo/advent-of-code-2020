#!/usr/bin/env python


required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

if __name__ == "__main__":
    valid = 0

    current = set()
    with open("input", "r") as fh:
        for line in fh:
            line = line.strip()

            if len(line) == 0:
                if len(required - current) == 0:
                    valid += 1

                current = set()

            for item in line.split():
                if len(item) > 4 and item[3] == ":":
                    current.add(item[:3])

    print(valid)
