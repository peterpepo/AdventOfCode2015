import os
import re
import itertools
from puzzle_commons.puzzle_commons import read_puzzle_input


class distancesMap():
    distances = {}  # Dictionary of distances, e.g ("City A", "City B"): 150

    def addDistance(self, pointFrom, pointTo, distance):
        """Adds distance between two points."""
        self.distances[(pointFrom, pointTo)] = int(distance)

    def getSymetricDistance(self, pointFrom, pointTo):
        """Returns distance from pointFrom to pointTo.
        Assumes, that distance from pointFrom to pointTo is same as in opposite direction"""
        distance = None

        try:
            distance = self.distances[(pointFrom, pointTo)]
        except KeyError:
            try:
                distance = self.distances[(pointTo, pointFrom)]
            except KeyError:
                pass

        return distance

    def getTotalDistance(self, points):
        """Returns total distance traveled when visiting points in given order."""
        total_distance = 0

        if len(points) > 1:
            for i in range(1, len(points)):
                total_distance += self.getSymetricDistance(points[i - 1], points[i])

        return total_distance

    def getNeighbours(self, point):
        """Returns set of points neighbouring with entered point."""
        neighbours = set(itertools.chain((route[1] for route in self.distances.keys() if route[0] == point),
                                         (route[0] for route in self.distances.keys() if route[1] == point)))

        return neighbours

    def getAllPoints(self):
        """Returns all points on the map."""
        allPoints = set(itertools.chain((route[1] for route in self.distances.keys()),
                                        (route[0] for route in self.distances.keys())))
        return allPoints


class Path():
    def __init__(self, visited_places=[], next_step=None):
        self.visited_places = visited_places[:]

        if next_step is not None:
            self.visited_places.append(next_step)

    def getVisitedPlaces(self):
        return self.visited_places

    def getCurrentPlace(self):
        if len(self.visited_places) > 0:
            return self.visited_places[len(self.visited_places)]


def is_shorter(distance1, distance2):
    """Compares two distances.
    Returns True, when distance1 < distance2.
    User for Part-A"""
    return distance1 < distance2


def is_longer(distance1, distance2):
    """Compares two distances.
    Returns True, when distance1 > distance2.
    User for Part-B"""
    return distance1 > distance2


def solve_part(is_better):
    """Solves puzzle_09, based on given evaluation function.
    Returns best path according to evaluation function."""
    puzzle_map = distancesMap()  # Distances between cities
    node_queue = []  # Queue of solutions to be processed
    best_known_solution = None  # Best known solution

    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_09_input.txt"):

        """Find instructions in format: (START_CITY) to (END_CITY) -> (DISTANCE)"""
        map_instruction = re.search(r"(\w+)\sto\s(\w+)\s=\s(\d+)", puzzle_input)

        if map_instruction is not None:
            puzzle_map.addDistance(map_instruction.group(1), map_instruction.group(2), map_instruction.group(3))

    """
    Add initial Path to get processed.
    At this stage, no city has been visited.
    """
    node_queue.append(Path())

    # Repeat, until there are no possible solutions to explored
    while len(node_queue) > 0:
        # Pick the first in queue
        current_path = node_queue.pop(0)

        """
        Check, whether explored path can be better (shorter/longer, depending on part A/B).
        If it's already worse then best known solution, it's not worth checking or exploring further.
        Example: If searching for shortest path, it's not worth visiting next place, if currently walked distance is already
            better then any existing solution.
        """
        # if best_known_solution is None or puzzle_map.getTotalDistance(
        #         current_path.getVisitedPlaces()) > puzzle_map.getTotalDistance(
        #     best_known_solution.getVisitedPlaces()):
        if best_known_solution is None or is_better(puzzle_map.getTotalDistance(current_path.getVisitedPlaces()),
                                                    puzzle_map.getTotalDistance(
                                                        best_known_solution.getVisitedPlaces())):

            # Check whether it's solution => all places have been visited
            if set(current_path.getVisitedPlaces()) == puzzle_map.getAllPoints():

                # Store as new best solution
                best_known_solution = current_path
            else:

                # Find which places need to be visited by substracting already visited from all places
                places_left_to_visit = (point for point in puzzle_map.getAllPoints() if
                                        point not in current_path.getVisitedPlaces())

                # Generate new possible solutions
                for place_to_visit in places_left_to_visit:
                    node_queue.append(Path(current_path.getVisitedPlaces(), place_to_visit))

    return best_known_solution, puzzle_map.getTotalDistance(best_known_solution.getVisitedPlaces())


def solve():
    path_part_a, path_part_a_distance = solve_part(is_shorter)
    print("Puzzle09, part A: goes through {}, distance of {}".format(path_part_a.getVisitedPlaces(),
                                                                     path_part_a_distance))

    path_part_b, path_part_b_distance = solve_part(is_longer)
    print("Puzzle09, part B: goes through {}, distance of {}".format(path_part_b.getVisitedPlaces(),
                                                                     path_part_b_distance))
