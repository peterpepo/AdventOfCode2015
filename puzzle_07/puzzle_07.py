import os
import re
from puzzle_commons.puzzle_commons import read_puzzle_input

# Dict of gates and instructions how to calculate it
gates = {}

# Dict of cached gate values (Once the gates has been calculated, store it's value
#  - program doesn't have to calculate deep recursion in case of register used multiple times
gates_cache = {}


def resolveGate(gate_name):
    global gates
    global gates_cache
    # Try to retrieve value from cache, in case it doesn't exist yet, continue
    try:
        return_value = gates_cache[gate_name]
        return return_value
    except KeyError:
        pass

    # Find instructions how to calculate gate
    try:
        gate = gates[gate_name]

        # In case of binary operations, get value of left operand
        if gate["leftOperand"] is not None:
            left_value = resolveGate(gate["leftOperand"])

        # There's always right operand (e.g unary operation NOT abc)
        right_value = resolveGate(gate["rightOperand"])

        # Calculate result, based on operator
        if gate["operator"] == "OR":
            return_value = left_value | right_value
        elif gate["operator"] == "AND":
            return_value = left_value & right_value
        elif gate["operator"] == "LSHIFT":
            return_value = left_value << right_value
        elif gate["operator"] == "RSHIFT":
            return_value = left_value >> right_value
        elif gate["operator"] == "NOT":
            return_value = ~right_value
        else:
            # No operator - simple value assignment (e.g, a -> b)
            return_value = right_value
    except KeyError:
        # If there's no instruction how to calculate, it must be a number
        return_value = int(gate_name)

    # Apply 16-bit mask on return value
    return_value = return_value & 0xffff

    # Cache value (Don't cache numbers, only register names)
    if not (gate_name.isdigit()):
        gates_cache[gate_name] = return_value
    return return_value


def solve():
    global gates
    global gates_cache

    # Load instructions
    for puzzle_input in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_07_input.txt"):
        """Regexp explanation:
        (?:([a-z0-9]+)\s){0,1} - optional group(1) of small letters/numbers - left operand
        (?:(OR|AND|LSHIFT|RSHIFT|NOT)\s){0,1}- optional operator - group(2)
        ([a-z0-9]+) - always present group(3) of small letters/numbers - right operand
        \s->\s - assignment notation (not captured in a group)
        (\w+) - group(4) - register name"""
        instruction_matcher = re.search(
            r"(?:([a-z0-9]+)\s){0,1}(?:(OR|AND|LSHIFT|RSHIFT|NOT)\s){0,1}([a-z0-9]+)\s->\s(\w+)", puzzle_input)

        # Check, whether line loaded from file is valid register operation
        if instruction_matcher is not None:
            gates[instruction_matcher.group(4)] = {
                "leftOperand": instruction_matcher.group(1),
                "operator": instruction_matcher.group(2),
                "rightOperand": instruction_matcher.group(3)
            }

    # PUZZLE07 - part A
    puzzle07_part_a = resolveGate("a")
    print("Puzzle07, part A:{}".format(puzzle07_part_a))

    # PUZZLE07 - part B
    # Add new instruction - assign solution from part A to wire-B
    gates["b"] = {"leftOperand": None, "operator": None, "rightOperand": str(puzzle07_part_a)}

    # Flush gates cache
    gates_cache = {}

    puzzle07_part_b = resolveGate("a")
    print("Puzzle07, part B:{}".format(puzzle07_part_b))
