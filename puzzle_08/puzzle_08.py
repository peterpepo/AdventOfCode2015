import os
import re
from puzzle_commons.puzzle_commons import read_puzzle_input

def part_a_replace(sourceMatcher):
    if sourceMatcher.group(0) is not None:
        return bytes(sourceMatcher.group(0), "utf-8").decode("unicode_escape")

def part_a(sourceString):
    remove_quotes = re.sub(r"^\"|\"$", "", sourceString)
    escape_g0_patterns = re.sub(r"\\(?:[\\\"]|x[a-f0-9][a-f0-9])",part_a_replace, remove_quotes)

    return escape_g0_patterns

def trim_quotes(sourceString):
    return re.sub(r"^\"|\"$", "", sourceString)

def part_b(sourceString):
    escape_g0_patterns = re.sub(r"(\\|\")", r"\\\1", sourceString)
    return escape_g0_patterns


def solve():
    puzzle_a_result = 0
    puzzle_b_result = 0

    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_08_input.txt"):
        # Total length + length of original input - length of string without quotes
        puzzle_a_result = puzzle_a_result + len(puzzle_input) - len(part_a(puzzle_input))
        puzzle_b_result = puzzle_b_result + len(part_b(puzzle_input)) - len(puzzle_input) + 2

    print("Puzzle08, part A:{}".format(puzzle_a_result))
    print("Puzzle08, part B:{}".format(puzzle_b_result))