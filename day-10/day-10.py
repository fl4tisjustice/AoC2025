from typing import cast

from functools import reduce
from collections import deque
import re

import scipy as sp

def get_input() -> list[tuple[int, tuple[int, ...], tuple[int, ...]]]:
    with open("day-10/input.txt", "r") as fl:
        raw = list(map(lambda line : line.rstrip("\n"), fl.readlines()))

    ret : list[tuple[int, tuple[int, ...], tuple[int, ...]]] = []
    for line in raw:
        lights_raw = cast(re.Match[str], re.search(r"(?<=\[)[.#]+(?=\])", line)).group()
        buttons_raw = list(map(lambda match : match.group(), re.finditer(r"(?<=\()([0-9]+,)*[0-9]+(?=\))", line)))
        joltages = tuple(map(int, cast(re.Match[str], re.search(r"(?<=\{)([0-9]+,)*[0-9]+(?=})", line)).group().split(",")))

        lights : int = reduce(lambda accum, curr : (accum << 1) | int(curr == "#"), lights_raw, 0)
        buttons : tuple[int, ...] = tuple(map(lambda button : reduce(lambda accum, curr : accum | (1 << (len(lights_raw) - curr - 1)), map(int, button.split(",")), 0), buttons_raw))
        ret.append((lights, buttons, joltages))
    return ret

def part_one(puzzle : list[tuple[int, tuple[int, ...], tuple[int, ...]]]) -> int:
    total_min_steps = 0
    for lights, buttons, _ in puzzle:
            queue : deque[tuple[int, int]] = deque()
            visited : set[int] = set()
            queue.append((0, 0))
            while len(queue):
                step, state = queue.popleft()
                if state in visited: continue
                if state == lights:
                     total_min_steps += step
                     break
                visited.add(state)
                queue.extend(map(lambda button : (step + 1, state ^ button), buttons))
    return total_min_steps

def part_two(puzzle : list[tuple[int, tuple[int, ...]]]) -> int:
    total_min_steps : float = 0.0
    for _, buttons, joltages in puzzle:
        A : list[tuple[int, ...]] = [[int(((1 << i) & button) != 0) for button in buttons] for i in range(len(joltages) - 1, -1, -1)]
        total_min_steps += sp.optimize.linprog([1] * len(buttons), A_eq = A, b_eq = joltages, integrality = 1).fun
    return int(total_min_steps)

def main() -> None:
    puzzle = get_input()
    print(f"Part One: { part_one(puzzle) } ")
    print(f"Part Two: { part_two(puzzle) } ")

if __name__ == "__main__":
    main()