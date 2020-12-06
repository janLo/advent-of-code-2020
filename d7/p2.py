#!/usr/bin/env python3

import re

_bag_regex = re.compile(r"^(?P<pref>(?P<color>[\w\s]+) bags contain ).*$")
_depends_regex = re.compile(r"(\d+) ([\w\s]+) bag[s]?(?:, |[.])")


def parse_rule(line):
    bag_match = _bag_regex.match(line)
    assert bag_match is not None, line

    enc_color = bag_match.group("color")
    contains = {}

    contains_line = line[len(bag_match.group("pref")) :]
    for count, color in _depends_regex.findall(contains_line):
        contains[color] = int(count)

    return enc_color, contains


SEARCH = "shiny gold"


if __name__ == "__main__":
    bag_dependencies = {}

    with open("input", "r") as fn:
        for line in fn:
            line = line.strip()
            color, dependencies = parse_rule(line)
            assert color not in bag_dependencies
            bag_dependencies[color] = dependencies

    all_count = 1

    next_search = [(SEARCH, 1)]

    while True:
        old_search = next_search
        next_search = []

        for s_color, s_cnt in old_search:
            for color, count in bag_dependencies[s_color].items():
                next_search.append((color, count * s_cnt))
                all_count += s_cnt * count

        if len(next_search) == 0:
            break

    print(all_count - 1)
