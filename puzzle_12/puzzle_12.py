import os
import json
from puzzle_commons.puzzle_commons import read_puzzle_input


def solve_puzzle12(input, ignore_red_objects=False):
    """Evaluates Day12 puzzle JSON by summing int values in object.
    
    Args:
        input: JSON to be evaluated
        ignore_red_objects (boolean): Determines, whether objects including "red" value shall be counted towards sum.
        
    Returns:
        int: sum of int objects in input JSON
    """
    # Total value of this object
    total_value = 0

    # Based on https://docs.python.org/3/library/json.html#json-to-py-table
    # Object translates into dict, array into list
    # If the chunk is object / array
    if isinstance(input, (dict, list)):

        # If value is object(dict)
        if isinstance(input, dict):
            # Check it's values
            input = input.values()
            # Whether it isn't forbidden (value == "red")
            for current in input:
                # In case, forbidden value is found, whole object is worthless, return value of 0
                if ignore_red_objects and current == "red":
                    return 0

        # Find value of all child objects
        for current in input:
            total_value += solve_puzzle12(current, ignore_red_objects)
    else:
        # If the input value isn't list, try parsing integer from it
        try:
            total_value = int(input)
        # Might be a string as well, in such case, value is 0
        except ValueError:
            total_value = 0

    return total_value


def solve():
    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_12_input.txt"):
        # Decode puzzle input into string
        decoded_json = json.loads(puzzle_input)
        # Get value, counting also "red" objects
        print("Puzzle12, part A:{}".format(solve_puzzle12(decoded_json, False)))
        # Get value ignoring "red" objects
        print("Puzzle12, part B:{}".format(solve_puzzle12(decoded_json, True)))
