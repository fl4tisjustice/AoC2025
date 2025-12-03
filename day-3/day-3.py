from itertools import combinations
from functools import reduce

def get_input() -> list[str]:
    with open("day-3/input.txt") as fl:
        banks : list[str] = list(map(lambda line : line.rstrip("\n"), fl.readlines()))
    return banks

def part_one(banks : list[str]) -> int:
    return reduce(lambda accum, curr : accum + max(map(lambda joltage : int("".join(joltage)), combinations(curr, 2))), banks, 0)

def part_two(banks : list[str]) -> int:
    total_joltage = 0
    for bank in banks:
        start_pos = 0
        joltage = 0
        length = len(bank)
        for i in range(12, 0, -1):
            idx, digit = reduce(lambda accum, curr : curr if curr[1] > accum[1] else accum, enumerate(list(map(int, list(bank[start_pos : length - i + 1])))))
            joltage = joltage * 10 + digit
            start_pos += idx + 1
        total_joltage += joltage
    return total_joltage

def main() -> None:
    banks : list[str] = get_input()
    print(f"Part One: { part_one(banks) }")
    print(f"Part Two: { part_two(banks) }")

if __name__ == "__main__":
    main()