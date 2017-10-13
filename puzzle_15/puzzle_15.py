# Puzzle A - ignore calories
def solve_brute_force():
    ingredients = {"Frosting":(4, -2, 0, 0, 5),
                   "Candy": (0, 5, -1, 0, 8),
                   "Butterscotch": (-1, 0, 5, 0, 6),
                   "Sugar": (0, 0, -2, 2, 1)}
    # PUZZLE-A
    # ingredients = {"Frosting":(4, -2, 0, 0),
    #                "Candy": (0, 5, -1, 0),
    #                "Butterscotch": (-1, 0, 5, 0),
    #                "Sugar": (0, 0, -2, 2)}

    ingredients_test = {"Butterscotch": (-1, -2, 6, 3),
                        "Cinnamon": (2, 3, -2, -1)}

    def variations_of_four_sum_hundred():
        variations = []

        max = 100
        max = max + 1

        for i in range (1,max-3):
            for j in range (1, max-2-i):
                for k in range(1, max-1-i-j):
                    yield((i,j, k, max-i-j-k-1))
                    # print(i,j, k, max-i-j-k-1)

    def get_score_puzzle_a(ingredients, amounts, puzzle_b = False):
        score_lines = []

        i = 0
        for ingredient in ingredients.values():
            score_line = []
            for ingredient_property in range(len(ingredient)):
                score_line.append(ingredient[ingredient_property] * amounts[i])

            score_lines.append(score_line)
            # print(score_line)
            i = i + 1

        cookie_properties = []

        for col in range(len(score_lines[0])):
            score = 0
            for line in score_lines:
                score = score + line[col]

            cookie_properties.append(score)


        if puzzle_b:
            if cookie_properties[4]!=500:
                return 0
        # print(cookie_properties)


        final_score = 1
        for subscore in cookie_properties:
            if subscore < 0:
                return 0

            final_score = final_score * subscore

        return final_score


    max_score = 0

    for variation in variations_of_four_sum_hundred():
        score = get_score_puzzle_a(ingredients, variation, puzzle_b=True)

        if score > max_score:
            max_score = score

    # print(get_score_puzzle_a(ingredients_test,(44,56)))

    print ("Max score is: {}".format(max_score))

solve_brute_force()

#
# a = ('a','b','c')
# print (a[0])

# print([1,2]*2)