#!/usr/bin/python
# filename: chapter1.py

# PROBLEM 1.1
# Implement an algorithm to determine if a string has a unique characters
def is_unique_str(input_str):
    appears = [False for i in range(0, 256)]
    for c in input_str:
        ascii_c = ord(c)
        if appears[ascii_c]:
            return False
        else:
            appears[ascii_c] = True

    return True


# PROBLEM 1.2
# Reverse a string, pay attention to null string
def reverse_string(input_str):
    if not input_str:
        return None
    
    chars = list(input_str)
    return ''.join(reversed(chars))

# PROBLEM 1.4
# Check whether two strings are anagram
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    map1 = {}
    map2 = {}

    for c in str1:
        if map1.has_key(c):
            map1[c] += 1
        else:
            map1[c] = 1

    for c in str2:
        if map2.has_key(c):
            map2[c] += 1
        else:
            map2[c] = 1

    for key, value in map1.items():
        if not map2.has_key(key) or map2[key] != value:
            return False;

    for key, value in map2.items():
        if not map1.has_key(key) or map1[key] != value:
            return False
    
    return True


# PROBLEM 1.5
# Replace space with '%20'
def replace_space(input_str):
    return str.replace(input_str, ' ', '%20')

# PROBLEM 1.6
# Rotate matrix
def rotate_matrix(matrix, clockwise=True):
    print 'Before rotate:'
    for row in matrix:
        print row

    row_count = len(matrix)
    column_count = len(matrix[0])
    if(row_count != column_count):
        print 'the matrix is not NxN'
        return None

    half = (row_count + 1) / 2
    print 'N=%d, half=%d'% (row_count, half)
    for i in range(half):
        for j in range(half):
            if(clockwise):
                #NW
                nw_temp = matrix[i][j]

                #SW
                sw_i = row_count - j - 1
                sw_j = i 
                matrix[i][j] = matrix[sw_i][sw_j]

                #SE
                se_i = row_count - i - 1
                se_j = row_count - j - 1
                matrix[sw_i][sw_j] = matrix[se_i][se_j]

                #NE
                ne_i = j
                ne_j = row_count - i - 1
                matrix[se_i][se_j] = matrix[ne_i][ne_j]
                matrix[ne_i][ne_j] = nw_temp
            else:
                print 'Not implemented'
                return None

    print 'after rotate:'
    for row in matrix:
        print row
    
    return matrix


# PROBLEM 1.7
# if an element in matrix is 0, then set all element as 0
def set_matrix_0_if_contains_0(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    row_0s = [False] * row_count
    column_0s = [False] * column_count

    for row in range(row_count):
        for column in range(column_count):
            if matrix[row][column] == 0:
                row_0s[row] = True
                column_0s[column] = True

    print 'Before set 0'
    for row in matrix:
        print row

    for i in range(row_count):
        for j in range(column_count):
            if row_0s[i] or column_0s[j]:
                matrix[i][j] = 0

    print 'After set 0'
    for row in matrix:
        print row


# PROBLEM 1.8
# check whether a string a rotation of another string. e.g. 'waterbottle' is a ratation of 'erbottlewat'
def check_ratation(str1, str2):
    if len(str1) != len(str2):
        return False
    str2str2 = str2 + str2
    return str1 in str2str2 



# MAIN FUNCTION
if __name__ == "__main__":
    str1 = 'waterbottle'
    str2 = 'erbottlewat'
    print check_ratation(str1, str2)
