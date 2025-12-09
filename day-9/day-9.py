from __future__ import annotations
from typing import Self
from math import sqrt
from itertools import combinations

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
    
def part_one(sparse_grid : list[Vector2D]) -> int:
    return max(map(lambda tiles : (vec := Vector2D(abs((res := tiles[1] - tiles[0]).x) + 1, abs(res.y) + 1)).x * vec.y, combinations(sparse_grid, 2)))

def main() -> None:
    sparse_grid = get_input()
    print(f"Part One: { part_one(sparse_grid) }")

if __name__ == "__main__":
    main()