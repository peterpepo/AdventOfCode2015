class Present:
    """Present"""
    def __init__(self, *dimensions):
        self.dimensions = dimensions

    def get_volume(self):
        """Returns volume of a present."""
        return self.dimensions[0]*self.dimensions[1]*self.dimensions[2]

    def get_two_smallest_dimensions(self):
        """Returns list of two smallest sides of a present"""
        # Copy list
        smallest_dimensions = list(self.dimensions)
        smallest_dimensions.remove(max(smallest_dimensions))

        return smallest_dimensions

    # Part-A
    def get_wrap(self):
        """Calculates wrap material required for a present"""
        wrap = 2*(self.dimensions[0]*self.dimensions[1]+self.dimensions[0]*self.dimensions[2]+self.dimensions[1]*self.dimensions[2])

        smallest_dimensions = self.get_two_smallest_dimensions()
        wrap += smallest_dimensions[0]*smallest_dimensions[1]

        return wrap

    # Part-B
    def get_ribbon(self):
        """Calculates ribbon required for a present"""
        smallest_dimensions = self.get_two_smallest_dimensions()

        return self.get_volume() + 2*(smallest_dimensions[0]+smallest_dimensions[1])


def solve():
    """"Prints solution for the Puzzle02"""
    from puzzle_commons.puzzle_commons import read_puzzle_input
    import os

    wrap_total = 0
    ribbon_total = 0

    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)),"puzzle_02_input.txt"):
        dimensions = puzzle_input.split("x")
        current_present = Present(int(dimensions[0]),int(dimensions[1]),int(dimensions[2]))

        wrap_total += current_present.get_wrap()
        ribbon_total += current_present.get_ribbon()

    print("Puzzle02, part A:", wrap_total)
    print("Puzzle02, part B:", ribbon_total)