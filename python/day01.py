#!/usr/bin/env python3

import fileinput
from typing import Iterable, Sequence


def calories(lines: Iterable[int]) -> list[int]:
    elves = []
    sum = 0
    for line in lines:
        if line:
            sum += line
        else:
            elves.append(sum)
            sum = 0
    return sorted(elves)


def part1(elves: Sequence[int]) -> int:
    return elves[-1]


def part2(elves: Sequence[int]) -> int:
    return sum(elves[-3:])


def main() -> None:
    lines = (int(ls) if (ls := line.strip()) else 0 for line in fileinput.input())
    elves = calories(lines)

    print("part1:", part1(elves))
    print("part2:", part2(elves))


if __name__ == "__main__":
    main()
