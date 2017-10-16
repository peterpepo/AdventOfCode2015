from puzzle_commons.puzzle_commons import read_puzzle_input
import os
import re
import queue

all_molecules = set()

initial_molecule = None

replacements = {}

def load_puzzle_input():
    global initial_molecule

    for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_19_input.txt"):
        if "=>" in puzzle_row:
            replace_from, replace_to = puzzle_row.split(" => ")
            replace_from.strip()
            replace_to = replace_to.strip()
            # print("{} to {}".format(replace_from, replace_to))

            mappings = replacements.get(replace_from, [])
            mappings = mappings + [replace_to]

            replacements[replace_from] = mappings
        else:
            initial_molecule = puzzle_row

    # for replacement in replacements:
    #     print("{} -> {}".format(replacement, replacements[replacement]))


def solve_a():
    total = 0
    for replacement in replacements:
        for replacement_alternative in replacements[replacement]:
            # print("Replacing {} by {}".format(replacement, replacement_alternative))

            pattern = re.compile(replacement)

            for current_match in pattern.finditer(initial_molecule):

                match_starting_at = current_match.start()


                replaced_string = initial_molecule[:match_starting_at]
                replaced_string = replaced_string + initial_molecule[match_starting_at:].replace(replacement, replacement_alternative,1)

                all_molecules.add(replaced_string)

    print("Total number of molecules: {}".format(len(all_molecules)))
    print("Total performed: {}".format(total))

def solve_b():

    # replacements = {
    #     "e" : ["H", "O"],
    #     "H" : ["HO", "OH"],
    #     "O" : ["HH"]
    # }

    prio_queue = queue.PriorityQueue()

    # # print(replacements)
    # def replace_molecule(initial_molecule, initial_length, medicine_molecule):
    #
    #     if initial_molecule == medicine_molecule:
    #         return initial_length
    #
    #     for replacement in replacements:
    #         new_molecules = []
    #
    #         for replacement_alternative in replacements[replacement]:
    #
    #             pattern = re.compile(replacement)
    #
    #             for current_match in pattern.finditer(initial_molecule):
    #                 match_starting_at = current_match.start()
    #
    #                 replaced_string = initial_molecule[:match_starting_at]
    #                 replaced_string = replaced_string + initial_molecule[match_starting_at:].replace(replacement,
    #                                                                                                  replacement_alternative,
    #                                                                                                  1)
    #
    #                 new_molecules.add(replaced_string)

    prio_queue.put((0, "e"))
    target_molecule = initial_molecule
    print(target_molecule)

    solution_found = False

    while solution_found != True:
        current_node = prio_queue.get()
        # print(current_node)
        current_length, current_molecule = current_node[0], current_node[1]

        if current_molecule == target_molecule:
            solution_found = True
        else:
            for replacement in replacements:

                for replacement_alternative in replacements[replacement]:

                    pattern = re.compile(replacement)

                    for current_match in pattern.finditer(current_molecule):
                        match_starting_at = current_match.start()

                        replaced_string = current_molecule[:match_starting_at]
                        replaced_string = replaced_string + current_molecule[match_starting_at:].replace(replacement,
                                                                                                         replacement_alternative,
                                                                                                         1)
                        prio_queue.put((current_length+1, replaced_string))





    print("Puzzle B: {}".format(current_length))

load_puzzle_input()
# solve_a()
solve_b()