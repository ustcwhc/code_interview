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


if __name__ == '__main__':
    print get_fibonacci(0)
    print get_fibonacci(1)
    print get_fibonacci(2)
    print get_fibonacci(3)
    print get_fibonacci(4)
    print get_fibonacci(5)
    print get_fibonacci(6)
    print get_fibonacci(7)
    print get_fibonacci(8)
    print get_fibonacci(9)
    print get_fibonacci(10)
    print get_fibonacci(11)
    print get_fibonacci(12)
