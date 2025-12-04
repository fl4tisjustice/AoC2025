from functools import reduce
from operator import add

from typing import cast

def get_input() -> list[str]:
    with open("day-4/input.txt", "r") as fl:
        return list(map(lambda line : line.rstrip("\n"), fl.readlines()))

def surrounding_paper_rolls(board : list[str], x : int, y : int) -> int:
    lower_y, upper_y = max(y - 1, 0), y + 1
    lower_x, upper_x = max(x - 1, 0), x + 2
    return (board[lower_y][lower_x : upper_x].count("@") if y > 0 else 0) + \
           board[y][lower_x : upper_x].count("@") - 1 + \
           (board[upper_y][lower_x : upper_x].count("@") if upper_y < len(board) else 0)

def part_one(board : list[str]) -> int:
    return len(list(filter(lambda counts : counts < 4, cast(list[int], reduce(add, list(map(lambda line : list(map(lambda pos : surrounding_paper_rolls(board, pos[0], line[0]), line[1])), enumerate(map(lambda line : filter(lambda pos : pos[1] == "@", enumerate(line)), board)))), [])))))

def part_two(board : list[str]) -> int:
    rolls = 0
    while True:
        removable = list(map(lambda line : list(filter(lambda counts : counts[1] < 4, map(lambda pos : (pos[0], surrounding_paper_rolls(board, pos[0], line[0])), line[1]))), enumerate(map(lambda line : filter(lambda pos : pos[1] == "@", enumerate(line)), board))))
        removed = len(reduce(add, removable))
        if removed == 0: break
        rolls += removed
        for i, line in enumerate(removable):
            for to_remove in line:
                idx, _ = to_remove
                board[i] = board[i][:idx] + "." + board[i][idx + 1:]
    return rolls

def main() -> None:
    board = get_input()
    print(f"Part One: { part_one(board) }")
    print(f"Part Two: { part_two(board) }")

if __name__ == "__main__":
    main()