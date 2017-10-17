def get_number_of_divisors(max_number):
    divisors_total = 0

    for i in range(1, max_number+1):
        if max_number % i == 0:
            divisors_total+=1

    return divisors_total

def solve_a_iterative():
    puzzle_input = 29000000
    divisors_min = puzzle_input // 10

    house_number = 1
    while get_number_of_divisors(house_number) <= divisors_min:
        house_number+=1

    print("Day20 puzzle-A: {}".format(house_number))

def solve_a_adding():
    puzzle_input = 29000000

    house = {}

    for i in range(1, puzzle_input):
        for j in range(i, puzzle_input, i):
            try:
                house[j] += i*10
            except KeyError:
                house[j] = i*10

    # print(house)

    for housenumber in house:
        if house[housenumber] >= puzzle_input:
            print("Day20 puzzle-A: {}".format(housenumber))
            break
    print("finished")

def solve_b_adding():
    puzzle_input = 29000000
    presents_delivered = 11

    house = {}

    for i in range(1, puzzle_input):
        for j in range(i, puzzle_input, i):
            if j > i*50:
                break
            try:
                house[j] += i*presents_delivered
            except KeyError:
                house[j] = i*presents_delivered

    # print(house)

    for housenumber in house:
        if house[housenumber] >= puzzle_input:
            print("Day20 puzzle-B: {}".format(housenumber))
            break
    print("finished")

# solve_a_iterative()
# solve_a_adding()
solve_b_adding()