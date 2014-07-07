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

# MAIN FUNCTION
if __name__ == "__main__":
    print reverse_string('abcdefg')


