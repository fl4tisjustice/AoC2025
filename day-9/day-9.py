from __future__ import annotations
from typing import Self, Iterable, cast
from math import sqrt
from itertools import combinations
from operator import attrgetter

class Vector2D:
    def __init__(self: Self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    
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
    
def get_input() -> list[Vector2D]:
    with open("day-9/input.txt", "r") as fl:
        return list(map(lambda line : Vector2D(*map(int, line.rstrip("\n").split(","))), fl.readlines()))

def largest_rect_area(rect_corners : Iterable[Vector2D, Vector2D]) -> int:
    return max(map(lambda tiles : (vec := Vector2D(abs((res := tiles[1] - tiles[0]).x) + 1, abs(res.y) + 1)).x * vec.y, rect_corners))

def part_one(sparse_grid : list[Vector2D]) -> int:
    return largest_rect_area(combinations(sparse_grid, 2))

def part_two(sparse_grid : list[Vector2D]) -> int:
    edges : list[tuple[Vector2D, Vector2D]] = list(zip(sparse_grid, sparse_grid[1:] + [sparse_grid[0]]))

    def has_no_instersections(rect : tuple[Vector2D, Vector2D]) -> bool:
        for from_tile, to_tile in edges:
            edge_top, edge_bottom = cast(list[int], sorted(map(attrgetter("y"), (from_tile, to_tile))))
            edge_left, edge_right = cast(list[int], sorted(map(attrgetter("x"), (from_tile, to_tile))))
            rect_top, rect_bottom = cast(list[int], sorted(map(attrgetter("y"), (rect[0], rect[1]))))
            rect_left, rect_right = cast(list[int], sorted(map(attrgetter("x"), (rect[0], rect[1]))))
            if edge_top < rect_bottom and rect_top < edge_bottom and edge_left < rect_right and rect_left < edge_right:
                return False
        return True

    return largest_rect_area(filter(has_no_instersections, combinations(sparse_grid, 2)))

def main() -> None:
    sparse_grid = get_input()
    print(f"Part One: { part_one(sparse_grid) }")
    print(f"Part Two: { part_two(sparse_grid) }")

if __name__ == "__main__":
    main()