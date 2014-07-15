#!/user/bin/python
# filename: chapter8.py


# PROBLEM 8.1
# Write a method to generate the nth Fibonacci number
# Solution 1: recursive method
def get_fibonacci(n):
    if n < 0:
        raise Exception('n in Fibonacci cannot be negative')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return get_fibonacci(n - 1) + get_fibonacci(n - 2)

# Solution 2: iterative method
def get_fibonacci_iter(n):
    if n < 0:
        raise Exception('n in Fibonacci cannot be negative')

    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1
    c = 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return c


# PROBLEM 8.2
# Write a algorithm to show all the path from left-up corner
# to right-down corner in a NxN grid
# Solution 1: recursive method
def move(x, y, n):
    node_str = '(' + str(x) + '-' + str(y) + ')'
    if x == n and y == n:
        return [node_str]

    paths = []
    if x < n:
        for path in move(x + 1, y, n):
            paths.append(node_str + ',' + path)
    if y < n:
        for path in move(x, y + 1, n):
            paths.append(node_str + ',' + path)
    return paths

# Solution 2: iterative method
def move_iter(n):
    start_node = (1, 1)
    paths = [[start_node]]
    next_paths = []
    step = 2 * (n - 1)

    for i in range(step):
        for path in paths:
            node = path[-1]

            # move right
            if node[0] < n:
                path_copy = list(path)
                path_copy.append((node[0] + 1, node[1]))
                next_paths.append(path_copy)

            # move down
            if node[1] < n:
                path_copy = list(path)
                path_copy.append((node[0], node[1] + 1))
                next_paths.append(path_copy)

        # copy path
        paths = next_paths
        next_paths = []

    for path in paths:
        print ','.join([('(' + str(node[0]) + '-' + str(node[1]) + ')')
                        for node in path])


# PROBLEM 8.3
# Write a method to return all the subsets of a set
# Solution 1: recursive method
def get_subsets(array):
    if not array or len(array) == 0:
        return [[]]

    top = array[0]
    remain = array[1:]
    remain_subsets = get_subsets(remain)
    subsets = []
    for remain_subset in remain_subsets:
        remain_subset_copy = list(remain_subset)

        # add subset without top
        subsets.append(remain_subset)

        # add subset with top
        remain_subset_copy.append(top)
        subsets.append(remain_subset_copy)

    return subsets

# Solution 2: iterative method
def get_subsets_iter(array):
    if not array or len(array) == 0:
        return [[]]

    subsets = [[]]
    next_subsets = []
    for i in range(len(array)):
        for subset in subsets:
            # add subset without i
            next_subsets.append(subset)

            # add subset with i
            subset_copy = list(subset)
            subset_copy.append(array[i])
            next_subsets.append(subset_copy)

        subsets = next_subsets
        next_subsets = []

    return subsets


# PROBLEM 8.4
# Write a method to compute all permutations of a string
# Solution 1: recursive method
def get_permutations(input_str):
    # no need to permute
    if not input_str or len(input_str) <= 1:
        return [input_str]

    first_char = input_str[0]
    remain_str = input_str[1:]
    remain_permutations = get_permutations(remain_str)

    permutations = []
    for remain_permutation in remain_permutations:
        for i in range(len(remain_permutation) + 1):
            permutations.append(
                remain_permutation[:i]
                + first_char
                + remain_permutation[i:])

    return permutations


# Solution 2: iterative method
def get_permutations_iter(input_str):
    # no need to permute
    if not input_str or len(input_str) <= 1:
        return [input_str]

    permutations = ['']
    next_permutations = []
    for i in range(len(input_str)):
        for permutation in permutations:
            for j in range(len(permutation) + 1):
                next_permutations.append(
                    permutation[:j]
                    + input_str[i]
                    + permutation[j:])

        permutations = next_permutations
        next_permutations = []

    return permutations


# PROBLEM 8.5
# Implement an algorithm to print all valid combinations of
# n-pairs of parentheses, Example:
# input: 3 (3 pairs of parentheses)
# output: ()()(), ()(()), (())(), ((())), (()())
# Solution 1: recursive method
def get_parentheses_combinations(bracket_count, right_need_count):
    if bracket_count < right_need_count or right_need_count < 0:
        raise Exception('error')

    if bracket_count == right_need_count:
        return [''.join(')' * right_need_count)]

    outputs = []
    # when right need count equals to 0, you can only
    # add ( at first, by bracket_count -= 1, and right_need_count = 1
    if right_need_count == 0:
        for combination in get_parentheses_combinations(bracket_count - 1, 1):
            outputs.append('(' + combination)

    # when right_need_count > 0, you can
    # 1. add '(' firstly, by bracket_count -= 1, and right_need_count += 1, or
    # 2. add ')' firstly, by bracket_count -= 1, and right_need_count -= 1
    else:
        for combination in get_parentheses_combinations(bracket_count - 1, right_need_count + 1):
            outputs.append('(' + combination)

        for combination in get_parentheses_combinations(bracket_count - 1, right_need_count - 1):
            outputs.append(')' + combination)

    return outputs


# Solution 2: iterative method
def get_parentheses_combinations_iter(n_pairs):
    # key: string
    # value: 1. steps remain; 2. right needed bracket count
    cur_dic = {'(': (2 * n_pairs - 1, 1)}

    # use for next/final round
    next_dic = {}
    finals = set()

    while len(cur_dic) > 0:
        for key, value in cur_dic.iteritems():
            # when right need count == remain count
            if value[0] == value[1]:
                key += ''.join(')' * value[0])
                finals.add(key)

            # when right needed count == 0, you can only add '('
            elif value[1] == 0:
                new_key = key + '('
                next_dic[new_key] = (value[0] - 1, 1)

            # when right needed count > 0, you can
            # 1. add '(' firstly, by value[0] -= 1, and right_need_count += 1
            # 2. add ')' firstly, by value[0] -= 1, and right_need_count -= 1
            else:
                new_key = key + '('
                next_dic[new_key] = (value[0] - 1, value[1] + 1)
                new_key = key + ')'
                next_dic[new_key] = (value[0] - 1, value[1] - 1)

        # for the next round
        cur_dic = next_dic
        next_dic = {}
    print 'Total', len(finals)
    return finals


# PROBLEM 8.6
# Replace an original color by a target color in a continuous area
def paint_full(
        x, y,
        min_x, min_y,
        max_x, max_y,
        original_color, target_color=None):
    # out of min/max
    if x < min_x or x > max_x or min_y < min_y or min_y > max_y:
        return False

    # set color
    if not target_color or get_color(x, y):
        set_color(x, y, target_color)

        if not target_color:
            target_color = get_color(x, y)

    # get color nearby
    if get_color(x - 1, y) == original_color:
        paint_full(x - 1, y, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x + 1, y) == original_color:
        paint_full(x + 1, y, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x, y - 1) == original_color:
        paint_full(x, y + 1, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x, y + 1) == original_color:
        paint_full(x, y + 1, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x - 1, y - 1) == original_color:
        paint_full(x - 1, y - 1, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x - 1, y + 1) == original_color:
        paint_full(x - 1, y + 1, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x + 1, y - 1) == original_color:
        paint_full(x + 1, y - 1, min_x, min_y, max_x, max_y, original_color, target_color)
    if get_color(x + 1, y + 1) == original_color:
        paint_full(x + 1, y + 1, min_x, min_y, max_x, max_y, original_color, target_color)
    return True

def set_color(x, y, target_color):
    pass

def get_color(x, y):
    pass

# PROBLEM 8.7
# Given an infinite number of quarters (25 cents), dimes (10 cents),
# nickels (5 cents) and pennies (1 cent), write code to calculate
# the number of ways of representing n cents
class CoinTypes:
    money_dic = {
        3: 25,
        2: 10,
        1: 5,
        0: 1
    }

def get_cent_represents(money, max_usage=3):
    if max_usage == 0:
        return 1

    divide = CoinTypes.money_dic[max_usage]
    max_q = money / divide
    method_count = 0

    for i in range(max_q + 1):
        money_left = money - i * divide
        method_count += get_cent_represents(money_left, max_usage - 1)

    return method_count


# PROBLEM 8.8
# Eight queen problem: in the 8x8 chess board, arrange 8 queens to avoid
# two queens in the same row, column or diagonal.
# Print all the methods
def arrange_queen(n, cur_row, queens=[]):
    valid_queens_list = []

    for col in range(n):
        queen = (cur_row, col)

        if is_valid(queen, queens):
            queens_copy = list(queens)
            queens_copy.append(queen)

            if cur_row == n - 1:
                valid_queens_list.append(queens_copy)
            else:
                for arrange in arrange_queen(n, cur_row + 1, queens_copy):
                    valid_queens_list.append(arrange)

    return valid_queens_list



def is_valid(queen, existed_queens):
    if not existed_queens:
        return True

    for existed_queen in existed_queens:
        # same row
        if queen[0] == existed_queen[0]:
            return False
        # same column
        if queen[1] == existed_queen[1]:
            return False

        # same diag
        if abs(queen[0] - existed_queen[0]) \
            == abs(queen[1] - existed_queen[1]):
            return False

    return True





# MAIN FUNCTION
if __name__ == '__main__':
    print len(arrange_queen(14, 0))



