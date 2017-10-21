from puzzle_commons.puzzle_commons import read_puzzle_input
import os
import itertools


def solve_a():
    numbers = []
    # TEST INPUT
    # for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_24_test_input.txt"):
    #     numbers.append(int(puzzle_row.strip()))

    print(sum(numbers)/3)
    # ACTUAL INPUT
    for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_24_input.txt"):
        numbers.append(int(puzzle_row.strip()))

    enquantum = None
    first_length = None
    # puzzle - A
    for i in range(len(numbers)-2):
        groups = itertools.combinations(numbers, i)

        # 1st level
        for group in groups:

            if sum(group) == sum(numbers)/3:
                if first_length is None:
                    first_length = len(group)
                elif len(group) > first_length:
                    return

                from operator import mul
                import functools

                if enquantum is None:
                    enquantum = functools.reduce(mul, group, 1)
                    print(enquantum)
                elif functools.reduce(mul, group, 1) >= enquantum:
                    return


                # print(group)
                reduced_group = numbers[:]
                for group_member in group:
                    reduced_group.remove(group_member)

                #2nd level
                for i in range(len(reduced_group) - 1):
                    groups2nd = itertools.combinations(reduced_group, i)

                    for group2nd in groups2nd:
                        if sum(group2nd) == sum(reduced_group) / 2:
                            # print(group)
                            reduced_group2nd = reduced_group[:]
                            for group_member2nd in group2nd:
                                reduced_group2nd.remove(group_member2nd)

                            # print("{}, {}, {}".format(group, group2nd, reduced_group2nd))
    print("Equantum: {}".format(enquantum))

def solve_b():
    numbers = []
    # TEST INPUT
    # for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_24_test_input.txt"):
    #     numbers.append(int(puzzle_row.strip()))

    print(sum(numbers)/4)
    # ACTUAL INPUT
    for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_24_input.txt"):
        numbers.append(int(puzzle_row.strip()))

    enquantum = None
    first_length = None
    # puzzle - B
    for i in range(len(numbers)-3):
        groups = itertools.combinations(numbers, i)

        # 1st level
        for group in groups:

            if sum(group) == sum(numbers)/4:
                if first_length is None:
                    first_length = len(group)
                elif len(group) > first_length:
                    return

                from operator import mul
                import functools

                if enquantum is None:
                    enquantum = functools.reduce(mul, group, 1)
                    print(enquantum)
                elif functools.reduce(mul, group, 1) >= enquantum:
                    return


                # print(group)
                reduced_group = numbers[:]
                for group_member in group:
                    reduced_group.remove(group_member)

                #2nd level
                for i in range(len(reduced_group) - 2):
                    groups2nd = itertools.combinations(reduced_group, i)

                    for group2nd in groups2nd:
                        if sum(group2nd) == sum(reduced_group) / 3:
                            # print(group)
                            reduced_group2nd = reduced_group[:]
                            for group_member2nd in group2nd:
                                reduced_group2nd.remove(group_member2nd)

                            # 3rd level
                            for i in range(len(reduced_group2nd) - 1):
                                groups3rd = itertools.combinations(reduced_group2nd, i)

                                for group3rd in groups3rd:
                                    if sum(group3rd) == sum(reduced_group2nd) / 2:
                                        # print(group)
                                        reduced_group3rd = reduced_group2nd[:]
                                        for group_member3rd in group3rd:
                                            reduced_group3rd.remove(group_member3rd)


                            # print("{}, {}, {}".format(group, group2nd, reduced_group2nd))
    print("Equantum: {}".format(enquantum))

def solve():
    numbers = []
    # Load test puzzle input
    for puzzle_row in read_puzzle_input(os.path.dirname(os.path.abspath(__file__)), "puzzle_24_test_input.txt"):
        numbers.append(int(puzzle_row.strip()))

    def split_in_equal_parts(list_of_numbers, parts):

        # Find all combinations of length 1 - (list_of_numbers-parts+1)
        ## e.g: there are 5 numbers to split in 3 groups;
        ### find combinations of 'up to 3' (5-3+1) = 3
        ### each group must contain at least 1 number
        max_comb_length = len(list_of_numbers)-parts+1

        for comb_length in range(1, max_comb_length):

            all_combinations = itertools.combinations(numbers, comb_length)

            # Check each combination, whether it gives sum of sum(list_of_numbers/parts)
            for tested_combination in all_combinations:
                if sum(tested_combination) == sum(list_of_numbers)/parts:


# solve_a()
# solve_b()
