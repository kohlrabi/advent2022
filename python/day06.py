#!/usr/bin/env python3

import fileinput
from typing import Iterable, Iterator, TypeVar
import collections
from itertools import islice

T = TypeVar("T")


def sliding_window(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    # taken from itertools doc
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def start_of_packet(line: str, same=4):
    for i, window in enumerate(sliding_window(line, same), start=same):
        if len(set(window)) == same:
            return i
    return len(line)


def part1(line: str) -> int:
    return start_of_packet(line, 4)


def part2(line: str) -> int:
    return start_of_packet(line, 14)


def main() -> None:
    lines = [line.strip("\n") for line in fileinput.input()]
    line = lines[0]

    print("part1:", part1(line))
    print("part2:", part2(line))


if __name__ == "__main__":
    main()
