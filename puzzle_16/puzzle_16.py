import os
from puzzle_commons.puzzle_commons import read_puzzle_input


def unpack_properties(properties_string):
    properties = {property_name.strip(): int(property_value.strip()) for property_name, property_value in
                  [property_string.split(":") for property_string in properties_string.split(",")]}
    return properties


def compare_aunts_puzzle_a(aunt_check, aunt_target):
    for property in aunt_check:
        if aunt_target.get(property, 0) != aunt_check[property]:
            return False

    return True


def compare_aunts_puzzle_b(aunt_check, aunt_target):
    greaterProperties = ("cats", "trees")
    lesserProperties = ("pomeranians", "goldfish")

    for property in aunt_check:
        aunt_target_property_value = aunt_target.get(property, 0)

        if ((property in greaterProperties and aunt_target_property_value > aunt_check[property]) or
                (property in lesserProperties and aunt_target_property_value < aunt_check[property])):
            return False
        elif (not (property in greaterProperties) and not (
            property in lesserProperties) and aunt_target_property_value != aunt_check[property]):
            return False

    return True


def solve():
    target_aunt_properties = """children: 3,
                                cats: 7,
                                samoyeds: 2,
                                pomeranians: 3,
                                akitas: 0,
                                vizslas: 0,
                                goldfish: 5,
                                trees: 3,
                                cars: 2,
                                perfumes: 1"""
    target_aunt_properties = unpack_properties(target_aunt_properties)

    puzzle_a_solution = None
    puzzle_b_solution = None

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_16_input.txt"):
        incorrect_aunt = False

        aunt_name, properties = puzzle_input.split(":", maxsplit=1)
        properties = unpack_properties(properties)

        # Check if solution for Puzzle_A, if it has not been found already
        if puzzle_a_solution is None:
            if compare_aunts_puzzle_a(properties, target_aunt_properties):
                puzzle_a_solution = aunt_name

        # Check if solution for Puzzle_B, if it has not been found already
        if puzzle_b_solution is None:
            if compare_aunts_puzzle_b(properties, target_aunt_properties):
                puzzle_b_solution = aunt_name

    print("Puzzle16, part A:{}".format(puzzle_a_solution))
    print("Puzzle16, part B:{}".format(puzzle_b_solution))
