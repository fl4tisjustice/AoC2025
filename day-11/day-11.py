from collections import deque
from functools import cache
from itertools import repeat, starmap
from enum import Flag, auto

def get_input() -> dict[str, set[str]]:
    with open("day-11/input.txt", "r") as fl:
        raw : list[str] = list(map(lambda line : line.rstrip("\n"), fl.readlines()))
    
    ret : dict[str, set[str]] = dict()

    for line in raw:
        in_dev, out_devs = line.split(": ")
        ret[in_dev] = set(out_devs.split(" "))
    
    return ret

def part_one(devices : dict[str, set[str]]) -> int:
    queue : deque[str] = deque()
    queue.append("you")

    paths = 0
    while len(queue):
        device = queue.popleft()
        if device == "out":
            paths += 1
            continue
        queue.extend(devices[device])
    return paths

class Route(Flag):
    NONE = 0
    DAC = auto()
    FFT = auto()
    BOTH = DAC | FFT

def part_two(devices : dict[str, set[str]]) -> int:
    @cache
    def dfs(device : str, route : Route = Route.NONE) -> int:
        if device == "out": return int(route == Route.BOTH)
        if device == "fft" or device == "dac":
            route |= Route.FFT if device == "fft" else Route.DAC
        return sum(starmap(dfs, zip(devices[device], repeat(route))))
    return dfs("svr")

def main() -> None:
    devices = get_input()
    print(f"Part One: { part_one(devices) }")
    print(f"Part Two: { part_two(devices) }")

if __name__ == "__main__":
    main()