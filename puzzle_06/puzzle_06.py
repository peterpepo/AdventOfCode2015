from puzzle_commons.Point import Point

class LightGrid():
    def __init__(self,sizeX, sizeY):
        self.lights = {}

        for i in range(sizeX+1):
            for j in range(sizeY+1):
                self.lights[Point(i,j)] = 0

    def __turnLightOn(self, pointToTurnOn):
        self.lights[pointToTurnOn] = 1

    def turnRangeOn(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self.__turnLightOn(Point(i, j))

    def __turnLightOff(self, pointToTurnOff):
        self.lights[pointToTurnOff] = 0

    def turnRangeOff(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self.__turnLightOff(Point(i, j))

    def __toggleLight(self, pointToToggle):
        if self.lights[pointToToggle] == 1:
            self.__turnLightOff(pointToToggle)
        else:
            self.__turnLightOn(pointToToggle)

    def toggleRange(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self.__toggleLight(Point(i, j))

    def getTotalBrightness(self):
        total_brightness = 0

        for brightness in self.lights.values():
            total_brightness += brightness

        return total_brightness

class DimmableLightGrid(LightGrid):

    def __turnLightOn(self, pointToTurnOn):
        self.lights[pointToTurnOn] += 1

    def __turnLightOff(self, pointToTurnOff):
        self.lights[pointToTurnOff] = max(self.lights[pointToTurnOff]-1, 0)

    def __toggleLight(self, pointToToggle):
        self.__turnLightOn(pointToToggle)
        self.__turnLightOn(pointToToggle)


def solve():
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    import re

    puzzle_part_A = LightGrid(999,999)
    puzzle_part_B = DimmableLightGrid(999,999)

    grids_to_operate = (puzzle_part_A, puzzle_part_B)


    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_06_input.txt"):
        import re

        lightInstructionMatcher = re.search(r"(toggle|(?<=turn.)on|off)\D+(\d+,\d+)\D+(\d+,\d+)", puzzle_input)

        if lightInstructionMatcher is not None:
            instruction = lightInstructionMatcher.group(1)
            (startX, startY) = [int(s) for s in lightInstructionMatcher.group(2).split(",")]
            (endX, endY) = [int(s) for s in lightInstructionMatcher.group(3).split(",")]


            for grid_to_operate in grids_to_operate:
                if instruction == "on":
                    grid_to_operate.turnRangeOn(startX, startY, endX, endY)
                elif instruction == "off":
                    grid_to_operate.turnRangeOff(startX, startY, endX, endY)
                elif instruction == "toggle":
                    grid_to_operate.toggleRange(startX, startY, endX, endY)

    print("Puzzle06, part A:{}".format(puzzle_part_A.getTotalBrightness()))
    print("Puzzle06, part B:{}".format(puzzle_part_B.getTotalBrightness()))