from typing import cast
from functools import reduce

def get_input() -> tuple[list[tuple[int, int]], list[int]]:
    with open("day-5/input.txt", "r") as fl:
        fresh_ranges, available = fl.read().split("\n\n")
    
    fresh_ranges = cast(list[tuple[int, int]], list(map(lambda rng : tuple(map(int, rng.split("-"))), fresh_ranges.split("\n"))))
    available = list(map(int, available.split("\n")))
    return fresh_ranges, available

def is_fresh(fresh_ranges : list[tuple[int, int]], ingredient : int) -> bool:
    for start, finish in fresh_ranges:
        if ingredient >= start and ingredient <= finish: return True
    return False

def part_one(fresh_ranges : list[tuple[int, int]], available : list[int]) -> int:
    return reduce(lambda accum, curr : accum + int(is_fresh(fresh_ranges, curr)), available, 0)

def overlap(left : tuple[int, int], right : tuple[int, int]):
    left_start, left_finish = left
    right_start, right_finish = right
    return (left_finish >= right_start and left_start <= right_finish) or (right_finish >= left_start and right_start <= left_finish)

def merge(accum : list[tuple[int, int]], curr : tuple[int, int]) -> list[tuple[int, int]]:
    if len(accum) == 0: return [curr]
    if not overlap(accum[-1], curr): return accum + [curr]
    accum[-1] = (min(accum[-1][0], curr[0]), max(accum[-1][1], curr[1]))
    return accum

def part_two(fresh_ranges : list[tuple[int, int]]):
    fresh_ranges.sort(key = lambda rng : rng[0])
    return reduce(lambda accum, curr : accum + curr[1] - curr[0] + 1, reduce(merge, fresh_ranges, []), 0)

def main():
    fresh_ranges, available = get_input()
    print(f"Part One: { part_one(fresh_ranges, available)}")
    print(f"Part Two: { part_two(fresh_ranges)}")

if __name__ == "__main__":
    main()