from pathlib import Path
from itertools import filterfalse


def read_input() -> [[int]]:
    p = Path('./inputs/day2.txt')

    ls = []
    with p.open() as fd:
        while line := fd.readline():
            ns = list(map(lambda n: int(n), line.split(' ')))
            ls.append(ns)

    return ls


def is_valid_report(l: [int]) -> bool:
    deltas = [x - y for (x, y) in zip(l, l[1:])]
    valid_incr = all(-1 >= d >= -3 for d in deltas)
    valid_decr = all( 1 <= d <=  3 for d in deltas)
    return valid_incr or valid_decr


def part1():
    ls = read_input()

    count = len(ls)
    for l in ls:
        if not is_valid_report(l):
            count -= 1

    # 369
    print(count)


def part2():
    ls = read_input()
    count = len(ls)

    for l in ls:
        if is_valid_report(l):
            continue

        fail_count = 0
        for i in range(len(l)):
            modified_report = l[:i] + l[i+1:]
            if is_valid_report(modified_report):
                break
            else:
                fail_count += 1

        if fail_count == len(l):
            count -= 1

    # 428
    print(count)


part1()
part2()

