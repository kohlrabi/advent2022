#!/usr/bin/env python3

from __future__ import annotations
from collections import deque
import fileinput
from typing import Sequence, Optional, Iterator


class Path:
    def __init__(self, name: str, size: Optional[int] = None) -> None:
        self.name = name
        self.children: dict[str, Path] = {}
        self.parent = None
        self._size = size

    def __iter__(self) -> Iterator[Path]:
        return iter(self.children.values())

    def append(self, path: Path) -> None:
        self.children[path.name] = path
        path.parent = self

    def __iadd__(self, path: Path) -> Path:
        self.append(path)
        return self

    def cd(self, path: str) -> Path:
        if path == "..":
            if self.parent is None:
                # root already
                return self
            return self.parent
        else:
            return self.children[path]

    def __getitem__(self, path: str) -> Path:
        return self.cd(path)

    def size(self) -> int:
        # file
        if self._size is not None:
            return self._size
        # dir
        size = 0
        for child in self.children.values():
            size += child.size()
        return size

    def is_dir(self) -> bool:
        return self._size is None

    def is_file(self) -> bool:
        return self._size is not None


def parse_tree(lines: Sequence[str]) -> Path:
    root = Path("/")
    curr = root

    for line in lines:
        ls = line.split()
        match ls[0]:
            case "$":
                # command
                match ls[1]:
                    case "cd":
                        match ls[2]:
                            case "/":
                                curr = root
                            case "..":
                                curr = curr[".."]
                            case _:
                                curr = curr[ls[2]]
            # listing
            case "dir":
                curr += Path(name=ls[1])
            case _:
                curr += Path(name=ls[1], size=int(ls[0]))

    return root


def part1(root: Path) -> int:
    total = 0
    d = deque([root])
    while d:
        curr = d.pop()
        s = curr.size()
        d.extend([d for d in curr if d.is_dir()])
        if s <= 100000:
            total += s
    return total


def part2(root: Path) -> int:
    max_size = 70000000
    total_size = root.size()
    free = max_size - total_size
    needed = 30000000 - free

    candidate = total_size
    d = deque([root])
    while d:
        curr = d.pop()
        s = curr.size()
        d.extend([d for d in curr if d.is_dir()])
        if s >= needed and s < candidate:
            candidate = s
    return candidate


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]
    root = parse_tree(lines)

    print("part1:", part1(root))
    print("part2:", part2(root))


if __name__ == "__main__":
    main()
