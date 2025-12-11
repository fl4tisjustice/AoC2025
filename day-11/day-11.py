from collections import deque

def get_input() -> dict[str, set[str]]:
    with open("day-11/input.txt", "r") as fl:
        raw : list[str] = list(map(lambda line : line.rstrip("\n"), fl.readlines()))
    
    ret : dict[str, set[str]] = dict()

    for line in raw:
        in_dev, out_devs = line.split(": ")
        ret[in_dev] = set(out_devs.split(" "))
    
    return ret

def part_one(devices : dict[str, set[str]]) -> int:
    visited : set[str] = set()
    queue : deque[str] = deque()

    queue.append("you")

    paths = 0
    while len(queue):
        device = queue.popleft()
        if device == "out":
            paths += 1
            continue
        visited.add(device)
        queue.extend(devices[device])
    
    return paths

def main() -> None:
    devices = get_input()
    print(f"Part One: { part_one(devices) }")

if __name__ == "__main__":
    main()