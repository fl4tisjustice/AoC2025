def str_to_range(string : str) -> tuple[int, int]:
    start, end = string.split("-")
    return (int(start), int(end))

def get_input() -> list[tuple[int, int]]:
    with open("day-2/input.txt", "r") as fl:
        raw : str = fl.read()
    return list(map(str_to_range , raw.split(",")))

def part_one(ranges : list[tuple[int, int]]) -> int:
    sum = 0
    for rng in ranges:
        for i in range(rng[0], rng[1] + 1):
            num_string = str(i)
            if len(num_string) % 2 != 0: continue
            left, right = num_string[:len(num_string) // 2], num_string[len(num_string) // 2:]
            if int(left) == int(right): sum += i
    return sum

def partition(n : int, i : int) -> list[int]:
    num_string : str = str(n)
    if len(num_string) % i != 0: return []
    return [int(num_string[idx : idx + i]) for idx in range(0, len(num_string), i)]

def part_two(ranges : list[tuple[int, int]]) -> int:
    sum = 0
    for rng in ranges:
        for i in range(rng[0], rng[1] + 1):
            if any(map(lambda size : len(set(partition(i, size))) == 1, range(1, len(str(i)) // 2 + 1))):
                sum += i
    return sum

def main() -> None:
    ranges = get_input()
    print(f"Part One: { part_one(ranges) }")
    print(f"Part Two: { part_two(ranges) }")

if __name__ == "__main__":
    main()