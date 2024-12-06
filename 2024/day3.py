from pathlib import Path
import re


def read_input() -> str:
    p = Path('./inputs/day3.txt')

    ls = []
    with p.open() as fd:
        while line := fd.readline():
            ls.append(line)

    return ls


def part1():
    ls = read_input()

    pattern = r'mul\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)'
    regex = re.compile(pattern)

    total = 0
    for l in ls:
        matches = regex.finditer(l)
        for match in matches:
            l = int(match.group('left'))
            r = int(match.group('right'))
            total += l * r

    print(total)


part1()



