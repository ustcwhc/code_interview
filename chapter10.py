#!/user/bin/python
# filename: chapter10.py

# PROBLEM 10.1
# Calculate the probability below
# Game1: try 1 and win 1
# Game2: try 3 and win 2 or 3
# Solution:
# Game1 = p
# Game2 = 3(1-p)p^2+p^3


# PROBLEM 10.2
# 3 ants on 3 vertices of a triangle
# what is the possibility of any two ants walk on the same sides
# general it to n ants and n vertices
# Solution:
# 1 - (1/2)^3*2 = 3/4
# 1 - (1/2)^n*2 = 1 - (1/2)^(n-1)


# PROBLEM 10.3
# Check whether two lines intersect in a plane
class Line(object):
    Epsilon = 0.000001
    def __init__(self, slope, y_intersect):
        self.Slope = slope
        self.Y_intersect = y_intersect

    def is_intersect(self, line2):
        return (self.Slope - line2.Slope) > Line.Epsilon \
               or (self.Y_intersect - line2.Y_intersect) < Line.Epsilon


# PROBLEM 10.4
# Write a method to implement -,*,/, you can only use + operation
def negative(n):
    pass

def minus(a, b):
    pass

def absolute(a):
    pass

def times(a, b):
    pass

def divide(a, b):
    pass

# PROBLEM 10.5
# Given two squares, show a line that could cut the squares into halves
# Solution: connect the centers of the squares


# PROBLEM 10.6
# Given a lot of points, find a line which passes the most number of points
# Solution: get all the lines between any two noes, calculate the same lines.
# counting by hashtable
# the most important things are:
# 1. override the hashcode method
# 2. override the equals method


# PROBLEM 10.7
# Find the kth number whose prime factor could only be 3, 5, and 7
def find_k_number(k):
    value = 1
    queue3 = [3]
    queue5 = [5]
    queue7 = [7]

    for i in range(k):
        value = min(queue3[0], queue5[0], queue7[0])
        if value == queue7[0]:
            queue7.pop(0)
        else:
            if value == queue5[0]:
                queue5.pop(0)
            else:
                queue3.pop(0)
                queue3.append(value * 3)
            queue5.append(value * 5)
        queue7.append(value * 7)
    return value


# MAIN FUNCTION
if __name__ == '__main__':
    print find_k_number(10)