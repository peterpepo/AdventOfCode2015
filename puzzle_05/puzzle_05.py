def isPartAValid(sourceString):
    import re

    # Regexp explanation: [aeiou]
    # contains any vowel (of group [aeiou])
    matches = re.findall(r"[aeiou]", sourceString)
    threeVowels = len(matches) >= 3

    # Regexp explanation: (\w)\1+
    # (\w) - any word character
    # \1+ - refernce to 1st consuming group repeated once or multiple times
    twoOrMoreSameCharsInARow = re.search(r"(\w)\1+", sourceString) is not None

    # Regexp explanation: (ab)|(cd)|(pq)|(xy)
    # contains any of sequences (ab) or (cd) or (pq) or (xy)
    forbiddenCombinations = re.search(r"(ab)|(cd)|(pq)|(xy)", sourceString) is not None

    return threeVowels and twoOrMoreSameCharsInARow and not forbiddenCombinations


def isPartBValid(sourceString):
    import re

    # Regexp explanation: (\w{2,}).*\1
    # (\w{2,}) - any two or more characters
    # .* - 0 or more (any characters)
    # \1 - first group repeated again
    containsTwoLetterRepeatWithoutOverlap = re.search(r"(\w{2,}).*\1", sourceString) is not None

    # Regexp explanation: (\w)(?!\1).\1
    # (\w) - any word char
    # (?!\1) - not followed by the same char from group1 (NOTE: lookahead doesn't consume characters)
    # . - any character (any which followed 1st group, but wasn't consumed by (?!\1))
    # \1 - 1st group repeated again
    containsRepeatOver = re.search(r"(\w)(?!\1).\1", sourceString) is not None

    return containsTwoLetterRepeatWithoutOverlap and containsRepeatOver


def solve():
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    partACount = 0
    partBCount = 0

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_05_input.txt"):

        if isPartAValid(puzzle_input):
            partACount += 1

        if isPartBValid(puzzle_input):
            partBCount += 1

    print("Puzzle05, part A:{}".format(partACount))
    print("Puzzle05, part B:{}".format(partBCount))