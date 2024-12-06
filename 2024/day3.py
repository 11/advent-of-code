from pathlib import Path
from collections import namedtuple
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


def part2():
    prgm = ''.join(read_input())

    mul_regex = re.compile(r'mul\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)')
    do_regex = re.compile(r'(do\(\))')
    dont_regex = re.compile(r'(don\'t\(\))')

    # get match objects
    Match = namedtuple('Match', ['span', 'group'])

    muls = [Match(match.span(), (match.group('left'), match.group('right'))) for match in mul_regex.finditer(prgm)]
    dos = [Match(match.span(), None) for match in do_regex.finditer(prgm)]
    donts = [Match(match.span(), None) for match in dont_regex.finditer(prgm)]
    ops = sorted([*muls, *dos, *donts], key=lambda m: m.span)

    # process multiplications after `do()`s
    total = 0
    can_process = True
    for match in ops:
        start, end = match.span
        cmd = prgm[start:end]

        is_do = cmd == 'do()'
        is_dont = cmd == 'don\'t()'
        is_mul = not is_do and not is_dont

        if is_do:
            can_process = True

        if is_dont:
            can_process = False

        if is_mul and can_process:
            l = int(match.group[0])
            r = int(match.group[1])
            total += l * r

    print(total)


part1()
part2()

