def getAdventCoin(salt, length):
    import hashlib

    counter = 1
    while True:
        # Value to be checked (input string, concatenated with counter)
        value_to_hash = salt + str(counter)

        # Create md5 hash object
        m = hashlib.new("md5",value_to_hash.encode())

        # Get hashed value in hex format
        value_hashed = m.hexdigest()

        # Check, whether the value conforms with criteria
        if value_hashed[0:length] == "0"*length:
            return counter

        counter += 1



def solve():
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_04_input.txt"):

        print("Puzzle04, part A:{}".format(getAdventCoin(puzzle_input, length=5)))
        print("Puzzle04, part B:{}".format(getAdventCoin(puzzle_input, length=6)))

