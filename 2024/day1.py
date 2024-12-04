from pathlib import Path


def read_input() -> ([int], [int]):
    p = Path('./inputs/day1.txt')

    l1 = []
    l2 = []
    with p.open() as fd:
        while line := fd.readline():
            n1, n2 = line.split()
            l1.append(int(n1))
            l2.append(int(n2))

    return l1, l2


def part1():
    l1, l2 = read_input()
    result = sum([abs(x - y) for (x, y) in zip(sorted(l1), sorted(l2))])
    print(result)


def part2():
    l1, l2 = read_input()

    counts = {}
    for n in l2:
        if counts.get(n, None) == None:
            counts[n] = 1
        else:
            counts[n] += 1

    result = sum([n * counts.get(n, 0) for n in l1])
    print(result)


part1()
part2()
