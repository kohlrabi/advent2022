#!/usr/bin/env python3

from copy import deepcopy
import fileinput
from math import ceil
import re
from typing import Iterable, Iterator, Sequence, TypeVar


_T = TypeVar("_T")


instruction_regex = re.compile(r"\D*(\d+)\D*(\d+)\D*(\d+)")


def enumerate_step(
    it: Iterable[_T], start: int = 0, step: int = 1
) -> Iterator[tuple[int, _T]]:
    for i in it:
        yield (start, i)
        start += step


def read_crates(lines: Sequence[str]) -> tuple[int, list[list[str]]]:
    crates: list[list[str]] = [list() for _ in range(ceil(len(lines[0]) / 4))]
    for i, line in enumerate(lines):
        if not line:
            break
        for j, crate in enumerate_step(crates, step=4):
            if line[j] == "[":
                crate.append(line[j + 1])
    crates = [crate[::-1] for crate in crates]
    return i, crates


def read_instructions(lines: Sequence[str]) -> list[tuple[int, ...]]:
    instructions = []
    for line in lines:
        m = instruction_regex.match(line)
        if m:
            instructions.append(tuple(map(int, m.groups())))
    return instructions


def part1(crates: list[list[str]], instructions: list[tuple[int, ...]]) -> str:
    for num, src, dest in instructions:
        for i in range(num):
            crates[dest - 1].append(crates[src - 1].pop())
    return "".join(crate[-1] for crate in crates if crate)


def part2(crates: list[list[str]], instructions: list[tuple[int, ...]]) -> str:
    for num, src, dest in instructions:
        crates[dest - 1].extend(crates[src - 1][-num:])
        del crates[src - 1][-num:]
    return "".join(crate[-1] for crate in crates if crate)


def main() -> None:
    lines = [line.strip("\n") for line in fileinput.input()]
    end_of_crates, crates = read_crates(lines)
    instructions = read_instructions(lines[end_of_crates:])

    print("part1:", part1(deepcopy(crates), instructions))
    print("part2:", part2(deepcopy(crates), instructions))


if __name__ == "__main__":
    main()
