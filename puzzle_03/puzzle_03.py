from puzzle_commons.Point import Point


class Carrier:

    def __init__(self):
        self.current_position = Point(0,0)

    def moveN(self):
        self.current_position =  Point(self.current_position.x, self.current_position.y+1)

    def moveS(self):
        self.current_position = Point(self.current_position.x, self.current_position.y - 1)

    def moveE(self):
        self.current_position = Point(self.current_position.x+1, self.current_position.y)

    def moveW(self):
        self.current_position = Point(self.current_position.x - 1, self.current_position.y)


def visitPoint(places_map, point_to_visit):
    try:
        visited_times = places_map[point_to_visit]
    except KeyError:
        visited_times = 0

    visited_times += 1

    places_map[point_to_visit] = visited_times


def solvePuzzle(carriers, visited_places):

    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os


    for carrier in carriers:
        visitPoint(visited_places, carrier.current_position)

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)),"puzzle_03_input.txt"):

        i = 0

        for direction in puzzle_input:

            current_carrier = carriers[i%len(carriers)]
            i += 1

            if direction == "<":
                current_carrier.moveW()
            elif direction == ">":
                current_carrier.moveE()
            elif direction == "^":
                current_carrier.moveN()
            else:
                current_carrier.moveS()

            visitPoint(visited_places, current_carrier.current_position)

def solve():

    # First puzzle
    first_puzzle_carriers = (Carrier(),)
    first_puzzle_visited_places = {}
    solvePuzzle(first_puzzle_carriers, first_puzzle_visited_places)
    print("Puzzle03, part A:{}".format(len(first_puzzle_visited_places)))

    # Second puzzle
    second_puzzle_carriers = (Carrier(), Carrier())
    second_puzle_visited_places = {}
    solvePuzzle(second_puzzle_carriers,second_puzle_visited_places)
    print("Puzzle03, part B:{}".format(len(second_puzle_visited_places)))
