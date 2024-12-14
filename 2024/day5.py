import sys
from pathlib import Path


def read_input(filepath: str) -> ([(int, int)],[[int]]):
    p = Path(filepath)

    rules = []
    updates = []

    seen_linebreak = False
    with p.open() as fd:
        while line := fd.readline():
            if line == '\n':
                seen_linebreak = True
                continue

            if not seen_linebreak:
                rule = line.split('|')
                before = int(rule[0])
                after = int(rule[1])
                rules.append((before, after))
            else:
                updates.append([int(num) for num in line.split(',')])

    return rules, updates


def is_valid_update(line: [int], rules: dict) -> bool:
    for idx, curr in enumerate(line):
        for num in range(idx+1, len(line)):
            afters = rules.get(num, set([]))
            if curr in afters:
                return False

    return True


def part1():
    filepath = sys.argv[1]
    rs, us = read_input(filepath)
    print(rs)
    rules = {}
    for rule in rs:
        before, after = rule
        if rules.get(before, None) is None:
            rules[before] = set([after])
        else:
            rules[before].add(after)

    valid_updates = []
    for line in us:
        if is_valid_update(line, rules):
            valid_updates.append(line)

    print(rules)

    score = 0
    for update in valid_updates:
        mid = int(len(update) / 2) + 1
        score += update[mid]

    print(score)

part1()
