import os
from puzzle_commons.puzzle_commons import read_puzzle_input

"""
Thanks to @Manuel Salvadores for answer posted here: https://stackoverflow.com/a/4633515
Note: I'm not the OP, just found it useful
"""
def get_combinations_of_sum (numbers, target_sum, partial=[]):

    current_sum = sum(partial)

    if current_sum == target_sum:
        yield partial
    elif current_sum > target_sum:
        return
    else:
        for i in range(len(numbers)):
            next_number = numbers[i]
            remaining = numbers[i+1:]
            yield from get_combinations_of_sum(remaining, target_sum, partial+[next_number])

def solve():
    puzzle_a_input = []

    # Read puzzle input
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_17_input.txt"):
        puzzle_a_input = puzzle_a_input + [int(puzzle_input)]

    def solve_puzzle_a():
        number_of_possibilities = 0

        for combination in get_combinations_of_sum(puzzle_a_input, 150):
            number_of_possibilities = number_of_possibilities + 1

        return number_of_possibilities

    def solve_puzzle_b():
        number_of_possibilities = 0
        minimal_length = None

        for combination in get_combinations_of_sum(puzzle_a_input, 150):
            if minimal_length is None or len(combination) < minimal_length:
                minimal_length = len(combination)

        for combination in get_combinations_of_sum(puzzle_a_input, 150):
            if len(combination) == minimal_length:
                number_of_possibilities = number_of_possibilities + 1

        return number_of_possibilities

    print("Puzzle17, part A:{}".format(solve_puzzle_a()))
    print("Puzzle17, part B:{}".format(solve_puzzle_b()))

