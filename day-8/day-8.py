from __future__ import annotations
from typing import Self
from math import sqrt
from itertools import combinations
from operator import mul
from functools import reduce
from collections import defaultdict, deque

class Vector3D:
    def __init__(self : Self, x : int, y : int, z : int) -> None:
        self.x : int = x
        self.y : int = y
        self.z : int = z
    
    def __add__(self: Self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self: Self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self: Self, scalar: int) -> Vector3D:
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self: Self, other: object) -> bool:
        return isinstance(other, Vector3D) and (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __hash__(self: Self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __lt__(self : Self, other : Vector3D) -> bool:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) < sqrt(other.x ** 2 + other.y ** 2 + other.z ** 2)

    def __repr__(self: Self) -> str:
        return f"({ self.x }, { self.y }, { self. z })"

def get_input() -> set[Vector3D]:
    with open("day-8/input.txt", "r") as fl:
        return set(map(lambda line : Vector3D(*map(int, line.rstrip("\n").split(","))), fl.readlines()))

def part_one(junction_boxes : set[Vector3D]) -> int:
    connections : defaultdict[Vector3D, set[Vector3D]] = defaultdict(set)
    
    shortest_connections : list[tuple[Vector3D, Vector3D, float]] = sorted(map(lambda pair : pair + (sqrt((pair[1].x - pair[0].x) ** 2 + (pair[1].y - pair[0].y) ** 2 + (pair[1].z - pair[0].z) ** 2),), combinations(junction_boxes, 2)), key = lambda tup : tup[2])
    
    for connection in shortest_connections[:1000]:
        box1, box2, _ = connection
        connections[box1].add(box2)
        connections[box2].add(box1)
    
    circuits : list[set[Vector3D]] = []
    visited : set[Vector3D] = set()
    for connection in connections:
        queue : deque[Vector3D] = deque()
        if connection in visited: continue
        queue.append(connection)
        circuit : set[Vector3D] = set()
        while len(queue):
            check : Vector3D = queue.pop()
            if check in visited: continue
            circuit |= { check, *connections[check] }
            queue.extend(connections[check])
            visited.add(check)
        circuits.append(circuit)

    return reduce(mul, sorted(map(len, circuits), reverse = True)[:3])

def part_two(junction_boxes : set[Vector3D]) -> int:
    connections : defaultdict[Vector3D, set[Vector3D]] = defaultdict(set)
    
    shortest_connections : list[tuple[Vector3D, Vector3D, float]] = sorted(map(lambda pair : pair + (sqrt((pair[1].x - pair[0].x) ** 2 + (pair[1].y - pair[0].y) ** 2 + (pair[1].z - pair[0].z) ** 2),), combinations(junction_boxes, 2)), key = lambda tup : tup[2])
    
    for connection in shortest_connections:
        box1, box2, _ = connection
        connections[box1].add(box2)
        connections[box2].add(box1)

        queue : deque[Vector3D] = deque()
        visited : set[Vector3D] = set()
        queue.append(box1)
        while len(queue):
            check : Vector3D = queue.pop()
            if check in visited: continue
            queue.extend(connections[check])
            visited.add(check)
        if len(visited) == 1000: return box1.x * box2.x
    return 0

def main() -> None:
    junction_boxes = get_input()
    print(f"Part One: { part_one(junction_boxes) }")
    print(f"Part Two: { part_two(junction_boxes) }")

if __name__ == "__main__":
    main()