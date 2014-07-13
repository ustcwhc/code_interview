#!/user/bin/python
# filename: chapter5.py

# PROBLEM 5.1
# You are given two 32b numbers, N and M, and two bit positions, i and j.
# Write a method to set all bits between i and j in N equal to M
# (e.g. M becomes a substring of N located a i and starting at j)
# Example:
# input N = 10000000000, M = 10101, i = 2, j = 6
# output N = 10001010100
def bton(n_str):
    n = 0
    for i in range(len(n_str)):
        n = n << 1
        if n_str[i] == '1':
            n += 1
    return n
def ntob(n):
    n_str = []
    while n > 0:
        bit = n % 2
        n_str.insert(0, str(bit))
        n = n >> 1
    if len(n_str) > 0:
        return ''.join(n_str)
    else:
        return '0'
def bit_substring(N_str, M_str, i, j):
    if i >= j:
        raise Exception('Input argument is wrong: i >= j')

    if i > 31 or j > 31:
        raise Exception('Input argument is wrong: i > 31 or j > 31')

    length = j - i + 1
    if len(M_str) != length:
        raise Exception('Input argument is wrong: M_str not equals the ' +
                        'length of (j - i + 1)')

    left_length = len(N_str) - j - 1
    right_start = len(N_str) - i

    return N_str[0:left_length] + M_str + N_str[right_start:]


# PROBLEM 5.2
# Convert a decimal number to binary
def ftob(float_str):
    point_index = -1

    # get positive
    negative_count = 0
    start_index = 0
    while float_str[start_index] == '-' or float_str[start_index] == '+':
        if float_str[start_index] == '-':
            negative_count += 1
        start_index += 1
    positive = negative_count % 2 == 0
    if positive:
        flag = ''
    else:
        flag = '-'

    # get point position
    for i in range(start_index, len(float_str)):
        if float_str[i] == '.':
            if point_index >= 0:
                raise Exception('Multi points appears in float_str')
            else:
                point_index = i
        elif float_str[i] < '0' or float_str[i] > '9':
            raise Exception('Error input char')

    # construct binary string
    if point_index < 0:
        # only has int part
        interger_str = float_str[start_index:]
        if len(interger_str) < 0:
            raise Exception('Input error, no numbers')
        else:
            binary_int_str = ntob(int(interger_str))
            binary_length = len(binary_int_str)
            if binary_length > 32:
                raise Exception('Input number is too large')
            return flag + ''.join(interger_str)
    else:
        # constains int and decimal parts
        interger_str = float_str[start_index:point_index]
        if len(interger_str) <= 0:
            binary_int_str = '0'
        else:
            binary_int_str = ntob(int(interger_str))

        decimal_part = float(float_str[point_index:])
        decimal_str = []
        while decimal_part > 0:
            if len(binary_int_str) + 1 + len(decimal_str) > 32:
                raise Exception('Input number is too long')
            decimal_part *= 2
            if decimal_part >= 1:
                decimal_str.append('1')
                decimal_part -= 1
            else:
                decimal_str.append('0')

        if len(binary_int_str) + 1 + len(decimal_str) > 32:
            raise Exception('Input number is too long')
        return flag + ''.join(binary_int_str) + '.' + ''.join(decimal_str)


# PROBLEM 5.3
# Given an interger, print the next smallest and next largest number
# that have the same number of 1 bits in their binary reprensentations
# (I don't quite understand the meaning of the problem)


# PROBLEM 5.4
# Explain what the following code does ((n & (n - 1)) == 0)
# Answer: verify whether n is the power of 2 or n equals to 0
def is_power_2(n):
    return (n & (n - 1)) == 0


# PROBLEM 5.5
# Write a function to show the number of bits needed to convert
# interger A to interger B
# For example: converting 101(5) to 010(2) needs 3 bits
def different_bits(A, B):
    bits = 0
    while A > 0 or B > 0:
        A_bit = A % 2
        B_bit = B % 2
        bits += A_bit ^ B_bit
        A = A >> 1
        B = B >> 1
    return bits


# PROBLEM 5.6
# Write a program to swap odd and even bits in an interger as few instructions
# as possible
def swap_odd_even(n):
    bits = []
    while n > 0:
        odd = n % 2
        n = n >> 1
        even = n % 2
        n = n >> 1
        bits.append(even)
        bits.append(odd)
    n_new = 0
    print bits
    while len(bits) > 0:
        n_new = (n_new << 1) + bits.pop()
    return n_new


# PROBLEM 5.7
# An array A[1...n] contains all the intergers from 0 to n except for one number
# which is missing. Find out this number by time complexity of O(n)
def find_missing(array, n):
    if len(array) != n:
        raise Exception('Argument is wrong: length of array not equals to n')

    binary_n = ntob(n)
    bit_num = len(binary_n)
    bit_1_counts = [0] * bit_num
    binary_former_array = ['0'] * bit_num
    binary_latter_array = ['0'] * bit_num
    for i in range(bit_num):
        binary_latter_array[i] = binary_n[i]

    for i in range(bit_num):
        bit_1_counts[i] = bton(''.join(binary_former_array)) / 2
        binary_latter_array[i] = '0'
        if binary_n[i] == '1':
            bit_1_counts[i] += 1 + bton(''.join(binary_latter_array))

        print '%d contains %d at position %d' % (n, bit_1_counts[i], bit_num - i)
        binary_former_array[i] = binary_n[i]

    for item in array:
        item_binary = ntob(item)
        item_binary_len = len(item_binary)
        for i in range(item_binary_len):
            index = bit_num + i - item_binary_len
            if item_binary[i] == '1':
                bit_1_counts[index] -= 1

    final_bits = []
    for bit_count in bit_1_counts:
        if bit_count > 0:
            final_bits.append('1')
        else:
            final_bits.append('0')

    return bton(''.join(final_bits))


# MAIN FUNCTION
if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 11
    missing = find_missing(array, n)
    print 'missing', missing