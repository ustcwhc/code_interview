#!/usr/bin/python
# filename: test.py

import random
import pdb


def partition(array, left, right, pivot_index):
    pivot_value = array[pivot_index]
    swap(array, pivot_index, right)
    store_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, store_index, i)
            store_index += 1
   
    swap(array, store_index, right)
    return store_index


def quicksort(array, left, right):
    if left < right:
        pivot_index = random.randint(left, right)
        store_index = partition(array, left, right, pivot_index)
        quicksort(array, left, store_index - 1)
        quicksort(array, store_index + 1, right)


def swap(input_array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp


# MAIN FUNCTION
if __name__ == '__main__':
    array = [3, 4, 5, 1, 56, 27, 82, 92, 100, 50]
    print array

    quicksort(array, 0, len(array) - 1)
    print array
