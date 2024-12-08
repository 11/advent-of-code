from pathlib import Path
import pdb


def read_input() -> [str]:
	p = Path('./inputs/day4.txt')

	ls = []
	with p.open() as fd:
		while line := fd.readline():
			ls.append(line)

	return ls


def s(i: int, j: int, ls: [str]) -> str:
	if i + 4 > len(ls):
		return ''

	return ls[i][j] + ls[i+1][j] + ls[i+2][j] + ls[i+3][j]


def e(i: int, j: int, ls: [str]) -> str:
	if j + 4 > len(ls):
		return ''

	return ls[i][j:j+4]


def se(i: int, j: int, ls: [str]) -> str:
	if i + 4 > len(ls) or j + 4 > len(ls):
		return ''

	return ls[i][j] + ls[i+1][j+1] + ls[i+2][j+2] + ls[i+3][j+3]


def sw(i: int, j: int, ls: [str]) -> str:
    if i + 4 > len(ls) or j - 3 < 0:
        return ''

    return ls[i][j] + ls[i+1][j-1] + ls[i+2][j-2] + ls[i+3][j-3]


def part1():
    ls = read_input()

    count = 0
    i = 0
    j = 0
    while i < len(ls):
        l = ls[i]
        while j < len(l):
            dirs = [s(i,j,ls), se(i,j,ls), sw(i,j,ls), e(i,j,ls)]
            res = list(filter(lambda x: x == 'XMAS' or x == 'SAMX', dirs))
            count += len(res)
            j += 1

        j = 0
        i += 1

    print(count)


part1()
