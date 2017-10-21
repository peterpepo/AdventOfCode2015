# Finds order in the source triangle, based on coordinations
"""
I would like to @Tehalynn (https://www.reddit.com/r/adventofcode/comments/3y5jco/day_25_solutions/cyaq55c/) for great help
on this function. I had idea of this solution since beginning, but couldn't figure out get_code_order() properly. THANKS!
While the rest of code might look similar / same, this is independent work of my own.
"""
def get_code_order(row_number, col_number):
    return sum(range(1, row_number+col_number-1)) + col_number

# Returns next number in sequence
def get_next_code(original_code):
    return (original_code*252533) % 33554393

code = 20151125
target_row = 2978
target_cel = 3083

# Find how many times we need to apply transformation
get_next_count = get_code_order(target_row, target_cel)-1

# Apply the transformation n-times
while get_next_count > 0:
    code = get_next_code(code)
    get_next_count -= 1

print("Day25 puzzle-A: {}".format(code))
