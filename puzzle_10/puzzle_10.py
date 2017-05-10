import os
from puzzle_commons.puzzle_commons import read_puzzle_input

def part_a(source_string):
    occurrences = 0
    last_character = None
    output_string = ""

    for current_character in source_string:
        if last_character is None:
            last_character = current_character
            occurrences += 1
            continue
        elif current_character != last_character:
            output_string = output_string + str(occurrences) + last_character
            last_character = current_character
            occurrences = 1
        else:
            occurrences += 1


    output_string = output_string + str(occurrences) + last_character

    return output_string



def solve():

    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_10_input.txt"):
        part_a_result = puzzle_input
        for i in range(50):
            part_a_result = part_a(part_a_result)

        print(len(part_a_result))

solve()