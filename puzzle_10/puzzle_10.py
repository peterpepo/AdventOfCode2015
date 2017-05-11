import os
from puzzle_commons.puzzle_commons import read_puzzle_input

def look_and_say(source_string):
    occurrences = 0
    output_string = ""

    # Go through whole string and 1 beyond
    for i in range(len(source_string) + 1):

        """Check whether we're past 0th character (to compare current with previous) AND
        (Previous character != current character OR we're already beyond last character)"""
        if i - 1 >= 0 and (i >= len(source_string) or source_string[i - 1] != source_string[i]):
            output_string = output_string + str(occurrences) + source_string[i - 1]
            occurrences = 1
        else:
            occurrences += 1

    return output_string

def solve():
    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_10_input.txt"):
        part_a_result = puzzle_input
        part_b_result = puzzle_input

        # Puzzle10 - part A
        for i in range(40):
            part_a_result = look_and_say(part_a_result)

        print("Puzzle10, part A:{}".format(len(part_a_result)))

        # Puzzle10 - part B
        # Note: runs very long
        for i in range(50):
            part_b_result = look_and_say(part_b_result)

        print("Puzzle10, part B:{}".format(len(part_b_result)))
