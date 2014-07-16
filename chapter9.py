#!/user/bin/python
# filename: chapter9.py
# topic: sorting and searching

import random

# Assistant method
def swap(array, i, j):
    if (i < 0
        or i >= len(array)
        or j < 0
        or j >= len(array)):
        raise Exception('index out of range of array')

    if i == j:
        return

    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# Bubble sort
def bubble_sort(array):
    print 'before sorting:', array
    for i in range(len(array) - 1):
        target = len(array) - 1 - i
        for j in range(target):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)

    print 'after sorting:', array


# Selection sort
def selection_sort(array):
    print 'before sorting:', array
    for i in range(len(array) - 1):
        _min_value = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < _min_value:
                _min_value = array[j]
                min_index = j
        swap(array, min_index, i)

    print 'after sorted:', array


# Merge sort:
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) / 2
    sub_array1 = merge_sort(array[:mid])
    sub_array2 = merge_sort(array[mid:])
    array_copy = [0] * len(array)

    for i in range(len(array_copy)):
        if not sub_array1:
            array_copy[i] = sub_array2.pop(0)
        elif not sub_array2:
            array_copy[i] = sub_array1.pop(0)
        else:
            if sub_array1[0] < sub_array2[0]:
                array_copy[i] = sub_array1.pop(0)
            else:
                array_copy[i] = sub_array2.pop(0)

    return array_copy


# Quick sort:
def partition(array, pivot_index):
    pivot_value = array[pivot_index]
    swap(array, pivot_index, len(array) - 1)

    pivot_real_index = 0
    for i in range(len(array) - 1):
        if array[i] < pivot_value:
            swap(array, i, pivot_real_index)
            pivot_real_index += 1

    swap(array, pivot_real_index, len(array) - 1)


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_index = random.randint(start, end)
    partition(array, pivot_index)

    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)


# Bucket sort
def bucket_sort(array, n):
    # get min and max
    min = array[0]
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
        if array[i] < min:
            min = array[i]

    # get step
    if max - min + 1 < n:
        n = max - min + 1
    step = (max - min + 1) / n

    # build buckets
    buckets = []
    min_i = min
    max_i = min + step - 1
    for i in range(n):
        buckets.append((min_i, max_i, []))
        min_i += step
        max_i += step

    # distribute items to each bucket
    for item in array:
        for bucket in buckets:
            if bucket[0] <= item <= bucket[1]:
                bucket[2].append(item)
                break

    # sort each bucket and concat together
    sorted_array = []
    for bucket in buckets:
        quick_sort(bucket[2], 0, len(bucket[2]) - 1)
        sorted_array.extend(bucket[2])

    return sorted_array


# PROBLEM 9.1
# Merge sorted array B into sorted array A.
# A has a large enough buffer to hold B
def merge_sort(A, B, n, m):
    last_whole = n + m - 1
    last_A = n - 1
    last_B = m - 1

    while last_A >= 0 and last_B >= 0:
        if A[last_A] < B[last_B]:
            A[last_whole] = B[last_B]
            last_whole -= 1
            last_B -= 1
        else:
            A[last_whole] = A[last_A]
            last_whole -= 1
            last_A -= 1

    while last_B >= 0:
        A[last_whole] = B[last_B]
        last_whole -= 1
        last_B -= 1


# PROBLEM 9.2
# Write a method to sort an array of strings so that all the anagrams
# are next to each other
def sort_string_array(string_array):
    print string_array
    string_array_pairs = []
    for item in string_array:
        string_array_pairs.append((item, ''.join(sorted(item))))

    string_array_pairs = sorted(string_array_pairs, key=lambda pair: pair[1])
    return [pair[0] for pair in string_array_pairs]


# PROBLEM 9.3
# Given a sorted array of n integers that has been rotated an unknown number
# of times, give an O(log n) algorithm to find an element in the array
def find_max_index(array, start, end):
    if start >= end:
        return start

    mid = (start + end) / 2
    if array[mid] > array[start] and array[mid] > array[end]:
        return find_max_index(array, mid, end)
    elif array[mid] < array[start] and array[mid] < array[end]:
        return find_max_index(array, start, mid)
    else:
        return end

def find_index(array, value, start, end):
    if start == end:
        if array[start] == value:
            return start
        else:
            return -1

    mid = (start + end) / 2
    if array[mid] > value:
        return find_index(array, value, start, mid - 1)
    elif array[mid] < value:
        return find_index(array, value, mid + 1, end)
    else:
        return mid

def find_index_rotate(array, value):
    max_index = find_max_index(array, 0, len(array) - 1)
    if value == array[max_index]:
        return max_index
    elif value > array[0]:
        return find_index(array, value, 0, max_index)
    else:
        return find_index(array, value, max_index + 1, len(array) - 1)



# PROBLEM 9.4
# If you have a 2GB file with one string per line, which sorting algorithm
# would you use to sort the file and why?
# Solution 1: bucket sort
# Sorting 2GB file will exceed the memory of a normal pc
# use bucket sort can reduce the memory in need


# PROBLEM 9.5
# Given a sorted array of strings which is interspersed with emtpy strings,
# write a method to find the location of a given string
def find_with_empty(str_array, target_str, start, end):
    if start >= end:
        if start == end and str_array[start] == target_str:
            return start
        else:
            return -1

    mid = (start + end) / 2
    mid_record = mid
    while str_array[mid] == '' and mid <= end:
        mid += 1

    if mid > end:
        return find_with_empty(str_array, target_str, start, mid_record - 1)

    if target_str == str_array[mid]:
        return mid
    elif target_str < str_array[mid]:
        return find_with_empty(str_array, target_str, start, mid - 1)
    else:
        return find_with_empty(str_array, target_str, mid + 1, end)


# PROBLEM 9.6
# Given a matrix in which each row and each column is sorted,
# write a method to find an element in it
def find_in_matrix(matrix, n):
    row = len(matrix)
    column = len(matrix[0])

    row_index = 0
    column_index = column - 1

    while row_index < row and column_index > 0:
        if n == matrix[row_index][column_index]:
            return row_index, column_index
        elif n < matrix[row_index][column_index]:
            column_index -= 1
        else:
            row_index += 1

    return -1, -1


# PROBLEM 9.7
# Given a list of bi-number, each bi-number consists of two numbers
# Write a method to sort the bi-numbers, get the possible longest
# line, where each bi-number is larger than the former one one both numbers
def sort_bi_numbers(bi_numbers):
    bi_numbers_wit_ids = {
        i: bi_numbers[i]
        for i in range(len(bi_numbers))
    }

    first_sort = [kv[0] for kv in
                  sorted(bi_numbers_wit_ids.iteritems(),
                         key=lambda kv: kv[1][0])]
    second_sort = [kv[0] for kv in
                   sorted(bi_numbers_wit_ids.iteritems(),
                          key=lambda kv: kv[1][1])]

def get_lcs(array1, array2):







# MAIN FUNCTION
if __name__ == '__main__':
    matrix = [[1, 4.5, 6, 7], [3, 5, 10, 12], [4, 7, 11, 15]]
    print find_in_matrix(matrix, 6)