MAX_POSITION : int = 100
START_POSITION : int = 50

def rotation_to_number(rotation : str) -> int:
    amount = int(rotation[1:])
    match rotation[0]:
        case "L": return -amount
        case "R": return amount
        case _:
            raise Exception("Invalid input")

def get_input() -> list[int]:
    with open("day-1/input.txt", "r") as fl:
        lines : map[str] = map(lambda line : line.rstrip("\n"), fl.readlines())
    
    try:
        rotations : list[int] = list(map(rotation_to_number, lines))
    except Exception as e:
        print(e)
        exit(1)

    return rotations

def part_one(rotations : list[int]) -> int:
    zero_count = 0
    position = START_POSITION
    for rotation in rotations:
        position = (position + rotation) % MAX_POSITION
        if position == 0: zero_count += 1
    return zero_count

def part_two(rotations : list[int]) -> int:
    zero_count = 0
    position = START_POSITION
    for rotation in rotations:
        dist : int = MAX_POSITION - position if rotation > 0 else -position
        if dist == 0: dist = MAX_POSITION if rotation > 0 else -MAX_POSITION
        if abs(rotation) >= abs(dist): zero_count += abs(int((rotation - dist) / MAX_POSITION)) + 1
        position = (position + rotation) % MAX_POSITION
    return zero_count

def main():
    rotations : list[int] = get_input()
    print(f"Part One: { part_one(rotations) }")
    print(f"Part Two: { part_two(rotations) }")

if __name__ == "__main__":
    main()