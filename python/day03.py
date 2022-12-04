#!/usr/bin/env python3

import fileinput
from typing import Iterator, Sequence, TypeVar


_T = TypeVar("_T")


def score(letter: str) -> int:
    if letter.islower():
        ret = ord(letter) - ord("a") + 1
    else:
        ret = ord(letter) - ord("A") + 27
    return ret


def triplets(seq: Sequence[_T]) -> Iterator[tuple[_T, _T, _T]]:
    yield from zip(seq[::3], seq[1::3], seq[2::3])


def part1(lines: Sequence[str]) -> int:
    total = 0
    for line in lines:
        length = len(line) // 2
        sets = set(line[:length]), set(line[length:])
        s = list(set.intersection(*sets))[0]  # should only be a single item
        total += score(s)
    return total


def part2(lines: Sequence[str]) -> int:
    total = 0
    for group in triplets(lines):
        sets = (set(g) for g in group)
        s = list(set.intersection(*sets))[0]  # should only be a single item
        total += score(s)
    return total


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]

    print("part1:", part1(lines))
    print("part2:", part2(lines))


if __name__ == "__main__":
    main()
