def count_floors(puzzle_input):
    result_floor = 0

    for instruction in puzzle_input:
        if instruction == '(':
            result_floor += 1
        else:
            result_floor -= 1

    return result_floor


def find_first_underground(puzzle_input):
    result_floor = 0

    for i in range(0, len(puzzle_input)):
        if puzzle_input[i] == '(':
            result_floor += 1
        else:
            result_floor -= 1

        if result_floor < 0:
            return i

    raise Exception("Never entered below ground")


def solve():
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)),"puzzle_01_input.txt"):
        print("Puzzle01, part A:", count_floors(puzzle_input))
        print("Puzzle01, part B:", find_first_underground(puzzle_input)+1)