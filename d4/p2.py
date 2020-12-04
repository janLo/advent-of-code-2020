#!/usr/bin/env python

import re


validators = {
    "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
    "iyr": re.compile(r"^(201[0-9]|2020)$"),
    "eyr": re.compile(r"^(202[0-9]|2030)$"),
    "hgt": re.compile(r"^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$"),
    "hcl": re.compile(r"^#[0-9a-f]{6}$"),
    "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
    "pid": re.compile(r"^[0-9]{9}$"),
}

if __name__ == "__main__":
    required = set(validators.keys())
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
                    name = item[:3]
                    if name != "cid" and name in validators:
                        if validators[name].match(item[4:].strip()) is not None:
                            current.add(name)
                        else:
                            print(
                                f"Item {name} ({item[4:]}) does not match {validators.get(name, None)}: {item}"
                            )

    print(valid)
