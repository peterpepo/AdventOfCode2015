from puzzle_commons.Point import Point

class LightGrid():
    def __init__(self,sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.lights = {}

        for i in range(sizeX+1):
            for j in range(sizeY+1):
                self.lights[Point(i,j)] = 0

    def _turnLightOn(self, pointToTurnOn):
        self.lights[pointToTurnOn] = 1

    def turnRangeOn(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self._turnLightOn(Point(i, j))

    def _turnLightOff(self, pointToTurnOff):
        self.lights[pointToTurnOff] = 0

    def turnRangeOff(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self._turnLightOff(Point(i, j))

    def _toggleLight(self, pointToToggle):
        if self.lights[pointToToggle] == 1:
            self._turnLightOff(pointToToggle)
        else:
            self._turnLightOn(pointToToggle)

    def toggleRange(self, startPointX, startPointY, endPointX, endPointY):
        for i in range (startPointX, endPointX+1):
            for j in range(startPointY, endPointY + 1):
                self._toggleLight(Point(i, j))

    def getTotalBrightness(self):
        total_brightness = 0

        for brightness in self.lights.values():
            total_brightness += brightness

        return total_brightness

    """
    I was curious, whether topaz (Eric Wastl) - AdventOfCode author is trying to tell us something.
    
    For this reason I decided to create heat-maps (https://en.wikipedia.org/wiki/Heat_map) for each solution (part A, part B).
    I used plotly library (https://plot.ly/) in it's basic form.
    
    For more information, check the website mentioned, namely https://plot.ly/python/heatmaps/ for heatmap.
    
    In order to draw the map, I used instructions from puzzle in [x;y] format.
    NOTE: THIS IS NOT REQUIRED TO SOLVE THE PUZZLES
    """
    def draw(self):
        import plotly
        import plotly.plotly as py
        import plotly.graph_objs as go

        # Visit https://plot.ly/python/heatmaps/, https://plot.ly/python/getting-started/ to get your user_name and api_key
        plotly.tools.set_credentials_file(username='PUT_YOUR_USER_NAME_HERE', api_key='PUT_YOUR_API_KEY_HERE')

        rows=[]
        for y in range(self.sizeY+1):
            row = []
            for x in range(self.sizeX+1):
                row.append(self.lights.get(Point(x,y)))

            rows.append(row)

        trace = go.Heatmap(z=rows)

        data = [trace]
        py.iplot(data, filename='basic-heatmap')


class DimmableLightGrid(LightGrid):

    def _turnLightOn(self, pointToTurnOn):
        self.lights[pointToTurnOn] += 1

    def _turnLightOff(self, pointToTurnOff):
        self.lights[pointToTurnOff] = max(self.lights[pointToTurnOff]-1, 0)

    def _toggleLight(self, pointToToggle):
        self._turnLightOn(pointToToggle)
        self._turnLightOn(pointToToggle)



def solve():
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    import re

    puzzle_part_A = LightGrid(999,999)
    puzzle_part_B = DimmableLightGrid(999,999)

    grids_to_operate = (puzzle_part_A, puzzle_part_B)


    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_06_input.txt"):

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

    # OPTIONAL: Draw HeatMaps
    # puzzle_part_A.draw()
    # puzzle_part_B.draw()
