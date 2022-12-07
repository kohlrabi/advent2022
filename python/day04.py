#!/usr/bin/env python3

import fileinput
from typing import Iterator, Sequence, TypeVar
import re


range_regexp = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


class Range:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __contains__(self, x: int) -> bool:
        return x >= self.start and x <= self.stop


def get_ranges(lines: Sequence[str]) -> Iterator[tuple[Range, Range]]:
    r = range_regexp
    for line in lines:
        m = r.match(line)
        if m:
            s1, e1, s2, e2 = map(int, m.groups())
            a = Range(s1, e1)
            b = Range(s2, e2)
            yield a, b
        else:
            raise ValueError("Invalid input")


def full_overlap(a: Range, b: Range) -> bool:
    return (b.start >= a.start and b.stop <= a.stop) or (
        a.start >= b.start and a.stop <= b.stop
    )


def partial_overlap(a: Range, b: Range) -> bool:
    return a.start in b or a.stop in b or b.start in a or b.stop in a


def part1(lines: Sequence[str]) -> int:
    fully_contained = 0
    for a, b in get_ranges(lines):
        fully_contained += full_overlap(a, b)
    return fully_contained


def part2(lines: Sequence[str]) -> int:
    partially_contained = 0
    for a, b in get_ranges(lines):
        partially_contained += partial_overlap(a, b)
    return partially_contained


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]

    print("part1:", part1(lines))
    print("part2:", part2(lines))


if __name__ == "__main__":
    main()
