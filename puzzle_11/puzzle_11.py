import re
import os
from puzzle_commons.puzzle_commons import read_puzzle_input

def containsSubsequent(sourceString):
    """Checks whether input string contains three alphabetically ordered characters (without skipping), eg: abc, xyz."""
    if len(sourceString) < 3:
        return False

    for i in range(len(sourceString)-2):
        if ord(sourceString[i]) == ord(sourceString[i+1])-1 == ord(sourceString[i+2])-2:
            return True

    return False

def containsForbidden(sourceString):
    """Checks whether input string contains any of forbidden characters i/o/l."""
    if len(re.findall(r"[iol]",sourceString)) > 0:
        return True
    else:
        return False

def containsTwoDifferentPairs(sourceString):
    """Checks whether input string contains two different pairs of characters."""
    pair_characters = set(character for character in re.findall(r"(?:(\w)\1)", sourceString))
    return len(pair_characters) >= 2

def isPuzzleAValid(sourceString):
    """Checks whether input is valid solution for puzzle A."""
    return containsSubsequent(sourceString) and not(containsForbidden(sourceString)) and containsTwoDifferentPairs(sourceString)


def decimalToAlphabet(sourceString):
    mapping = {i-ord("a"):chr(i) for i in range(ord("a"), ord("z")+1)}

    current = int(sourceString)

    output_string = ""

    while current != 0:
        remainder = current % len(mapping)
        remainder_string = mapping[remainder]

        output_string = remainder_string + output_string

        current = current // len(mapping)

    return output_string


def alphabetToDecimal(sourceString):
    mapping = {chr(i): i-ord("a") for i in range(ord("a"), ord("z") + 1)}

    output_number = 0

    for i in range(len(sourceString)-1, -1, -1):
        current_number = mapping[sourceString[i]]
        add_to_total = pow(len(mapping), len(sourceString)-1-i) * current_number
        output_number += add_to_total

    return output_number


def getPaddedPassword(sourceString, length):
    """Padds string from left to desired length."""
    return (length-len(sourceString))*'a'+sourceString

def solve_a(start_password):
    for i in range(alphabetToDecimal(start_password)+1, alphabetToDecimal("zzzzzzzz")+1):
        if(isPuzzleAValid(getPaddedPassword(decimalToAlphabet(i),8))):
            return getPaddedPassword(decimalToAlphabet(i),8)


def solve():
    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle11_input.txt"):
        print("Puzzle11, part A:{}".format(solve_a(puzzle_input)))
        print("Puzzle11, part B:{}".format(solve_a(solve_a(puzzle_input))))
