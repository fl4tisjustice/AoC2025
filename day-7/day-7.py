from __future__ import annotations
from typing import Self
from math import sqrt

class Vector2D:
    def __init__(self: Self, x: int, y: int):
        self.x: int = x;
        self.y: int = y;
    
    def __add__(self: Self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self: Self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self: Self, scalar: int) -> Vector2D:
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self: Self, other: object) -> bool:
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y
    
    def __hash__(self: Self) -> int:
        return hash((self.x, self.y))

    def __lt__(self: Self, other: Vector2D) -> bool:
        return sqrt(self.x ** 2 + self.y ** 2) < sqrt(other.x ** 2+ other.y ** 2)
    
    def __repr__(self: Self) -> str:
        return f"({self.x}, {self.y})"

def get_input() -> tuple[Vector2D, list[Vector2D], int]:
    with open("day-7/input.txt", "r") as fl:
        raw = fl.readlines()

    splitters : list[Vector2D] = []
    for i in range(2, len(raw), 2):
        splitters += list(map(lambda splitter : Vector2D(splitter[0], i), filter(lambda pair : pair[1] == "^", enumerate(raw[i]))))
    
    start = Vector2D(raw[0].find("S"), 0)
    return start, splitters, len(raw)

LEFT = Vector2D(-1, 0)
RIGHT = Vector2D(1, 0)
def part_one(start : Vector2D, splitters : list[Vector2D], height : int) -> int:
    rays : set[Vector2D] = set()
    rays.add(start)

    split_count = 0
    for i in range(2, height):
        targets = list(filter(lambda splitter : splitter.y == i, splitters))
        new_rays = rays.copy()
        for ray in rays:
            splits = list(filter(lambda res : res.x == 0, map(lambda target : target - ray, targets)))
            if len(splits) == 0: continue

            for split in splits:
                splitter = split + ray
                new_rays |= {splitter + LEFT, splitter + RIGHT}
                split_count += 1
            new_rays.remove(ray)
        rays = set(map(lambda ray : Vector2D(ray.x, i), new_rays))

    return split_count

def main() -> None:
    start, splitters, height = get_input()
    print(f"Part One: { part_one(start, splitters, height) }")

if __name__ == "__main__":
    main()