#!/usr/bin/env python3

from __future__ import annotations
import fileinput
from typing import Sequence, Any

Grid_T = list[list[int]]


def transpose(lst: Sequence[Any]) -> list[Any]:
    return list(map(list, zip(*lst)))


def parse_grid(lines: Sequence[str]) -> Grid_T:
    ret = [[int(x) for x in line] for line in lines]
    return ret


def visible_rowwise(grid: Grid_T, visible: Grid_T, reverse: bool = False) -> None:
    for row, vis in zip(grid, visible):
        last_max = -1
        if reverse:
            row = row[::-1]
        for j, elem in enumerate(row):
            if elem > last_max:
                if reverse:
                    j = -j - 1
                vis[j] = 1
                last_max = elem


def part1(grid: Grid_T) -> int:
    visible = [[0 for _ in row] for row in grid]

    visible_rowwise(grid, visible, False)
    visible_rowwise(grid, visible, True)

    grid = transpose(grid)
    visible = transpose(visible)

    visible_rowwise(grid, visible, False)
    visible_rowwise(grid, visible, True)

    return sum(x for row in visible for x in row)


def part2(grid: Grid_T) -> int:
    pass


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]
    arr = parse_grid(lines)

    print("part1:", part1(arr))
    print("part2:", part2(arr))


if __name__ == "__main__":
    main()
