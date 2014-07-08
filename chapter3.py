#!/usr/bin/python
# filename: chapter2.py

# CLASS
class Node(object):

    def __init__(self, data):
        self.Data = data 
        self.Next = None

    def append(self, node):
        if not self:
            return None

        cur_node = self
        while cur_node.Next:
            cur_node = cur_node.Next
        
        cur_node.Next = node
        return self

    def setNext(self, node):
        if node:
            node.Next = self.Next
        self.Next = node

    def print_list(self):
        cur_node = self
        while cur_node:
            print cur_node.Data.__str__() + ',',
            cur_node = cur_node.Next
        print

# STACK CLASS
class Stack(object):
    def __init__(self):
        self.Count = 0
        self._head = None

    def push(self, node):
        if self.Count == 0:
            self._head = node
            node.Next = None
            self.Count = 1
        else:
            node.Next = self._head
            self._head = node
            self.Count += 1

    def pop(self):
        if self.Count == 0:
            return None
        else:
            top = self._head
            self.Count -= 1
            
            if self.Count == 0:
                self._head = None
            else:
                self._head = self._head.Next

            return top

    def peek(self):
        return self._head


# QUEUE CLASS
class Queue(object):
    def __init__(self):
        self.Count = 0
        self._head = None
        self._tail = None

    def enqueue(self, node):
        if self.Count == 0:
            self._head = node
            self._tail = node
            node.Next = None
            self.Count = 1
        else:
            self._tail.Next = node
            self._tail = node
            node.Next = None
            self.Count += 1

    def dequeue(self):
        if self.Count == 0:
            return None
        else:
            top = self._head
            self.Count -= 1

            if self.Count == 0:
                self._head = None
                self._tail = None
            else:
                self._head = self._head.Next

            return top

    def peek(self):
        return self._head


# PROBLEM 3.1
# Using a single array to implement three stacks
class ArrayStack(object):
    def __init__(self, array, start_index, max_count):
        # error
        if start_index < 0 or start_index >= len(array):
            raise 'Start index is out of range of array'
        if max_count <= 0:
            raise 'max count of stack is not positive'
        if start_index + max_count - 1 >= len(array):
            raise 'end index is out of range of array'

        self._array = array
        self._start_index = start_index
        self._max_count = max_count
        self._end_index = start_index + max_count - 1
        self.Count = 0
        self._head_index = start_index - 1
        self._min = -1

    def push(self, node):
        if self.Count == 0:
            self._array[self._start_index] = node
            self._head_index = self._start_index
            self.Count = 1
            self._min = node
        elif self._head_index < self._end_index:
            self._array[self._head_index + 1] = node
            self._head_index += 1
            self.Count += 1
            
            #record min
            if(node < self._min):
                self._min = node
        else:
            print 'There is no enough space for stack'
            return False

        return True

    def pop(self):
        if self.Count == 0:
            return None
        else:
            top = self._array[self._head_index]
            self._head_index -= 1
            self.Count -= 1
            return top

# PROBLEM 3.2
# Get the minimum element in O(1) time
    def get_min(self):
        if self.Count > 0:
            return self._min
        else:
            print 'There is no element'
            return -1

# PROBLEM 3.3
# Implement a set a stacks, which contains several stacks, when one stack is full
# then move to another stack
class SetOfStackes(object):
    def __init__(self, max_count):
        self._max_count = max_count
        self._stacks = []

        array = [0] * max_count
        self._stacks.append(ArrayStack(array, 0, max_count))
        self._cur_stack = 0

    def push(self, item):

                
# MAIN FUNCTION
if __name__ == '__main__':
    length = 100
    array = [i for i in range(100)]
    step = length / 3
    start1 = 0
    length1 = step
    start2 = start1 + length1
    length2 = step
    start3 = start2 + length2
    length3 = length - length1 - length2

    stack1 = ArrayStack(array, start1, length1)
    stack2 = ArrayStack(array, start2, length2)
    stack3 = ArrayStack(array, start3, length3)

    stack2.push(1)
    stack2.push(10)
    stack2.push(100)
    print stack2.get_min()
