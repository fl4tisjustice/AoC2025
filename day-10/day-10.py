from typing import cast

from functools import reduce
from collections import deque
import re

def get_input() -> list[tuple[int, tuple[int, ...]]]:
    with open("day-10/input.txt", "r") as fl:
        raw = list(map(lambda line : line.rstrip("\n"), fl.readlines()))

    ret : list[tuple[int, tuple[int, ...]]] = []
    for line in raw:
        lights_raw = cast(re.Match[str], re.search(r"(?<=\[)[.#]+(?=\])", line)).group()
        buttons_raw = list(map(lambda match : match.group(), re.finditer(r"(?<=\()([0-9]+,)*[0-9]+(?=\))", line)))
        # joltage_raw = list(map(lambda match : match.group(), re.finditer(r"(?<=\{)([0-9]+,)*[0-9]+(?=})", line)))

        lights : int = reduce(lambda accum, curr : (accum << 1) | int(curr == "#"), lights_raw, 0)
        buttons : tuple[int, ...] = tuple(map(lambda button : reduce(lambda accum, curr : accum | (1 << (len(lights_raw) - curr - 1)), map(int, button.split(",")), 0), buttons_raw))
        ret.append((lights, buttons))
    return ret

def part_one(puzzle : list[tuple[int, tuple[int, ...]]]) -> int:
    total_min_steps = 0
    for lights, buttons in puzzle:
            queue : deque[tuple[int, int]] = deque()
            visited : set[int] = set()
            queue.append((0, 0))
            while len(queue):
                step, state = queue.popleft()
                if state == lights:
                     total_min_steps += step
                     break
                visited.add(state)
                queue.extend(filter(lambda light : light[1] not in visited, map(lambda button : (step + 1, state ^ button), buttons)))
    return total_min_steps

def main() -> None:
    print(f"Part One: { part_one(get_input()) } ")

if __name__ == "__main__":
    main()