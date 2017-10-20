from puzzle_commons.puzzle_commons import read_puzzle_input
import os

class SimpleComputer():
    def __init__(self, instructions):
        self.registers = {"a": 0, "b": 0}
        self.instructions = instructions
        self.instruction_position = 0

    # Half
    def hlf(self, register_name):
        self.registers[register_name] /= 2
        self.jmp()

    # Triple
    def tpl(self, register_name):
        self.registers[register_name] *= 3
        self.jmp()

    # Increment
    def inc(self, register_name):
        self.registers[register_name] += 1
        self.jmp()

    # Jump
    def jmp(self, offset=1):
        self.instruction_position += int(offset)

    # Jump-if-even
    def jie(self, register_name, offset):
        if self.registers[register_name]%2==0:
            self.instruction_position += int(offset)
        else:
            self.jmp()

    # Jump-if-one
    def jio(self, register_name, offset):
        if self.registers[register_name]==1:
            self.instruction_position += int(offset)
        else:
            self.jmp()

    # Get register value
    def get_registers(self):
        return self.registers

    # Process instructions
    def process_instructions(self):

        while self.instruction_position<len(self.instructions):
            # Load instruction
            current_instruction = self.instructions[self.instruction_position]

            # Get instruction name (split instruction on 1st space)
            instruction_name, instruction_parameters = current_instruction.split(" ", 1)
            instruction_parameters = instruction_parameters.split(", ")

            if instruction_name == "hlf":
                self.hlf(instruction_parameters[0])
            elif instruction_name == "tpl":
                self.tpl(instruction_parameters[0])
            elif instruction_name == "inc":
                self.inc(instruction_parameters[0])
            elif instruction_name == "jmp":
                self.jmp(instruction_parameters[0])
            elif instruction_name == "jie":
                self.jie(instruction_parameters[0], instruction_parameters[1])
            elif instruction_name == "jio":
                self.jio(instruction_parameters[0], instruction_parameters[1])

# Special type of SimpleComputer, with register a=1
class SimpleComputerPB(SimpleComputer):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.registers["a"] = 1



def solve():
    computer_instructions = []

    # TEST INPUT
    # for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_23_test_input.txt"):

    # ACTUAL INPUT
    for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_23_input.txt"):
        computer_instructions.append(puzzle_row.strip())


    puzzle_a = SimpleComputer(computer_instructions)
    puzzle_a.process_instructions()
    print("Day-23 puzzle-A solution: {}".format(puzzle_a.get_registers()["b"]))

    puzzle_b = SimpleComputerPB(computer_instructions)
    puzzle_b.process_instructions()
    print("Day-23 puzzle-B solution: {}".format(puzzle_b.get_registers()["b"]))
