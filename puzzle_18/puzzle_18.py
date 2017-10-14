from puzzle_commons.Point import Point
from puzzle_commons.puzzle_commons import read_puzzle_input
import os
import re


class LightGrid():
    def __init__(self):
        self.grid_state = [[]]

    def print_state(self):
        # print(self.grid_state)
        for row in self.grid_state:
            for column in row:
                print(column, end="")
            print()

    def set_grid_state(self, state):
        for row in range(len(state)):
            for column in range(len(state[row])):
                if state[row][column] == ".":
                    state[row][column] = 0
                else:
                    state[row][column] = 1

        self.grid_state = state

    def neighbours_score(self, row, col):
        score = 0

        for other_row in range(row-1, row+2):
            for other_col in range(col-1, col+2):
                # print("getting ROW:{}, COL:{}".format(other_row, other_col))
                if (other_row != row or other_col!=col) and (other_row>=0 and other_row<len(self.grid_state) and other_col>=0 and other_col<len(self.grid_state[other_row])):
                        score = score + self.grid_state[other_row][other_col]
                        # print("got: {}".format(self.grid_state[other_row][other_col]))

        return score

    def get_brightness(self):
        score_total = 0
        for row in self.grid_state:
            for column in row:
                score_total = score_total + column

        return score_total


    def animate_puzzle_a(self):
        # Deepcopy
        new_state = [[column for column in range(len(self.grid_state[row]))] for row in range(len(self.grid_state))]
        for row in range(len(self.grid_state)):
            for col in range(len(self.grid_state[row])):
                current_state = self.grid_state[row][col]
                neighbours_score = self.neighbours_score(row, col)

                if current_state == 1:
                    if neighbours_score == 2 or neighbours_score == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0
                else:
                    if neighbours_score == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0

        #puzzle_b
        # new_state[0][0] = 1
        # new_state[0][len(self.grid_state[0])-1] = 1
        # new_state[len(self.grid_state)-1][0] = 1
        # new_state[len(self.grid_state)-1][len(self.grid_state[len(self.grid_state)])-1] = 1
        new_state[0][0] = 1
        new_state[0][99] = 1
        new_state[99][0] = 1
        new_state[99][99] = 1

        self.grid_state = new_state



def solve():
    # for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_18_input.txt"):
    puzzle_a_state = [[puzzle_column for puzzle_column in puzzle_row.strip()] for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_18_input.txt")]

    lightGridPuzzleOne = LightGrid()
    lightGridPuzzleOne.set_grid_state(puzzle_a_state)

    for i in range(100):
        lightGridPuzzleOne.animate_puzzle_a()
    print(lightGridPuzzleOne.get_brightness())
