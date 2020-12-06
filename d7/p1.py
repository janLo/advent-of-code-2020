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

    enc_bags = set()

    for color, dependencies in bag_dependencies.items():
        if SEARCH != color and SEARCH in dependencies:
            enc_bags.add(color)

    while True:
        pass_enc_bags = set()
        for enc_bag in enc_bags:
            for color, dependencies in bag_dependencies.items():
                if (
                    color != SEARCH
                    and color not in enc_bags
                    and enc_bag in dependencies
                ):
                    pass_enc_bags.add(color)

        enc_bags.update(pass_enc_bags)

        if len(pass_enc_bags) == 0:
            break

    print(len(enc_bags))
