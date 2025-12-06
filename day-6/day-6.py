from typing import Callable, Literal, cast
from operator import add, mul
from functools import reduce
import re

def str_to_op(string : Literal["+", "*"]) -> Callable[[int, int], int]:
    match string:
        case "*": return mul
        case "+": return add

def solve(problems : list[tuple[list[int], Callable[[int, int], int]]]):
    return reduce(lambda accum, curr : accum + reduce(curr[1], curr[0]), problems, 0)

def part_one() -> int:
    with open("day-6/input.txt", "r") as fl:
        raw = fl.readlines()
    
    numbers : list[list[int]] = list(map(list, zip(*map(lambda line : list(map(int, re.findall("[0-9]+", line))), raw[:-1]))))
    operators : list[Callable[[int, int], int]] = list(map(str_to_op, re.findall(r"[+*]", raw[-1])))

    problems = list(zip(numbers, operators))
    
    return solve(problems)

def part_two() -> int:
    with open("day-6/input.txt", "r") as fl:
        raw = fl.readlines()
    
    widths : list[int] = list(map(len, re.findall(r" +", raw[-1], re.M)))

    problems : list[list[str]] = []
    offset = 0
    for i, width in enumerate(widths):
        problems.append(reduce(lambda accum, curr : accum + [curr[offset : offset + width + int(i == len(widths) - 1)]], raw[:-1], cast(list[str], [])))
        offset += width + 1

    reordered_problems : list[list[int]] = list(map(lambda problem : list(map(lambda numbers : int("".join(numbers)), zip(*problem))), problems))
    operators : list[Callable[[int, int], int]] = list(map(str_to_op, re.findall(r"[+*]", raw[-1])))

    return solve(list(zip(reordered_problems, operators)))

def main() -> None:
    print(f"Part One: { part_one() }")
    print(f"Part Two: { part_two() }")

if __name__ == "__main__":
    main()