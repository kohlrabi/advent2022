#!/usr/bin/env python3

import fileinput
from typing import Sequence


def tally(lines: Sequence[str], combinations: dict[str, int], scores: dict[str, int]):
    return sum(combinations[line] + scores[line[-1]] for line in lines)


def part1(lines: Sequence[str]) -> int:
    combinations = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }

    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    return tally(lines, combinations, scores)


def part2(lines: Sequence[str]) -> int:
    combinations = {
        "A X": 3,
        "A Y": 1,
        "A Z": 2,
        "B X": 1,
        "B Y": 2,
        "B Z": 3,
        "C X": 2,
        "C Y": 3,
        "C Z": 1,
    }

    scores = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    return tally(lines, combinations, scores)


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]

    print("part1:", part1(lines))
    print("part2:", part2(lines))


if __name__ == "__main__":
    main()
