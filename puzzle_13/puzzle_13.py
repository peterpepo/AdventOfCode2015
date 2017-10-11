import os
import itertools
from puzzle_commons.puzzle_commons import read_puzzle_input


def solve():
    score_dict = {}
    all_names = set()

    def get_score(guest_pair):
        try:
            return score_dict[guest_pair[0], guest_pair[1]]
        except KeyError:
            try:
                return score_dict[guest_pair[1], guest_pair[0]]
            except KeyError:
                return 0

    def add_score(guest_pair, score_diff):
        try:
            current_score = score_dict[guest_pair]
        except KeyError:
            try:
                guest_pair = (guest_pair[1], guest_pair[0])
                current_score = score_dict[guest_pair]
            except KeyError:
                current_score = 0

        score_dict[guest_pair] = current_score + score_diff

    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_13_input.txt"):

        # Split puzzle input by whitespace
        puzzle_input_split = puzzle_input.split(" ")

        # Based on sample input of "Alice would gain 54 happiness units by sitting next to Bob."
        person_one = puzzle_input_split[0]                                      #0th is the first person name
        person_two = puzzle_input_split[10].replace("\n","").replace(".","")    #10th is second person name; trim off newline and/or trailing dot
        pair_score = int(puzzle_input_split[3])                                 #3rd is gain/lose

        # In case, instruction says lose, flip it's value
        if puzzle_input_split[2] == "lose":
            pair_score = -pair_score

        # Add decoded score to total score of this pair
        add_score((person_one, person_two), pair_score)

        # Add both ends of decoded pair to SET
        all_names.add(person_one)
        all_names.add(person_two)

    def solve_puzzle():
        # All possible permutations (order is important, elements does not repeat) of seating plan
        all_permutations = list(itertools.permutations(all_names, len(all_names)))

        max_score = None

        for sitting in all_permutations:

            current_score = 0

            # Add score of each pair to total score
            for i in range(-1, len(sitting)-1):

                current_score = current_score + get_score((sitting[i], sitting[i+1]))

            # If new score is greater than maximum found until now, save it
            if max_score is None or current_score > max_score:
                max_score = current_score

        return max_score

    print("Puzzle13, part A:{}".format(solve_puzzle()))

    all_names.add(str()) # Add some empty String object to list of all names, representing "myself"
    print("Puzzle13, part B:{}".format(solve_puzzle()))
