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


    def is_empty(self):
        return self.Count == 0

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

    def is_empty(self):
        return self.Count == 0

# PROBLEM 3.1
# Using a single array to implement three stacks
class ArrayStack(object):
    def __init__(self, array, start_index, max_count):
        # error
        if start_index < 0 or start_index >= len(array):
            raise Exception('Start index is out of range of array')
        if max_count <= 0:
            raise Exception('max count of stack is not positive')
        if start_index + max_count - 1 >= len(array):
            raise Exception('end index is out of range of array')

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

    def peek(self):
        if self.Count == 0:
            return None
        else:
            return self._array[self._head_index]

    def print_arraystack(self):
        print self._array[:self.Count]

    def is_empty(self):
        return self.Count == 0

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
class SetOfStacks(object):
    def __init__(self, max_count):
        self._max_count = max_count
        self._stacks = []

        self._stacks.append(ArrayStack([0] * max_count, 0, max_count))
        self._cur_stack = 0

    def push(self, item):
        if not self._stacks[self._cur_stack].push(item):
            self._stacks.append(ArrayStack([0] * max_count, 0, max_count))
            self._cur_stack += 1
            self._stacks[self._cur_stack].push(item)
        
        return True

    def pop(self):
        top = self._stacks[self._cur_stack].pop()
        while not top and self._cur_stack > 0:
            self._cur_stack -= 1
            top = self._stacks[self._cur_stack].pop()

        if top:
            return top
        elif self._cur_stack == 0:
            return self._stacks[0].pop()
        else:
            return None

    def pop_at(self, index):
        if index > self._cur_stack:
            raise Exception('input index is out of range of the stacks')
        else:
            return self._stacks[index].pop()
          
    def print_stacks(self):
        for i in range(self._cur_stack + 1):
            for j in range(self._stacks[i].Count):
                print self._stacks[i]._array[j],
            if self._stacks[i].Count > 0:
                print '|',
        print


# PROBLEM 3.4
# Implement the movement algorithm for Towers of Hanoi, 
# which contains 3 rods and N disks
class Hanoi(object):
    def __init__(self, n):
        array1 = [0] * n
        array2 = [0] * n
        array3 = [0] * n

        self._stack1 = ArrayStack(array1, 0, n)
        self._stack2 = ArrayStack(array2, 0, n)
        self._stack3 = ArrayStack(array3, 0, n)

        self._stack1.push(3)
        self._stack1.push(2)
        self._stack1.push(1)

        print 'Before moving:'
        self.print_stacks()

    def move_1_to_3(self, n):
        # error detection
        if self._stack1.Count < n:
            raise Exception('There are no %d disks on stack1'%d, n)

        if n == 1:
            self.move_1_to_2(1)
            self.move_2_to_3(1)
        else:
            # step1: move top n-1 disks from stack1 to stack3
            self.move_1_to_3(n - 1)

            # step2: move last disk from stack1 to stack2
            self.move_1_to_2(1)

            # step3: move top n-1 disks from stack3 to stack1
            self.move_3_to_1(n - 1)

            # step4: move last disk from stack2 to stack3
            self.move_2_to_3(1)

            # step5: move top n-1 disks from stack1 to stack3
            self.move_1_to_3(n - 1)

        # finished
        self.print_stacks()

    def move_1_to_2(self, n):
        # error detection
        if self._stack1.Count < n:
            raise Exception('There are no %d disks on stack1'%d, n)
        
        if n == 1:
            top = self._stack1.pop()
            if (self._stack2.Count <= 0 or top < self._stack2.peek()):
                self._stack2.push(top)
            else:
                raise Exception('Error movement of %d on %d'% (top, self._stack2.peek()))
        else:
            # step1: move top n-1 disks from stack1 to stack3
            self.move_1_to_3(n - 1)

            # step2: move last disk from stack1 to stack2
            self.move_1_to_2(1)

            # step3: move top n-1 disks from stack3 to stack2
            self.move_3_to_2(n - 1)

        # finished
        self.print_stacks()

    def move_2_to_1(self, n):
        # error detection
        if self._stack2.Count < n:
            raise Exception('There are no %d disks on stack2'%d, n)
       
        if n == 1:
            top = self._stack2.pop()
            if (self._stack1.Count <= 0 or top < self._stack1.peek()):
                self._stack1.push(top)
            else:
                raise Exception('Error movement of %d on %d'% (top, self._stack1.peek()))
        else: 
            # step1: move top n-1 disks from stack2 to stack3
            self.move_2_to_3(n - 1)

            # step2: move last disk from stack2 to stack1
            self.move_2_to_1(1)

            # step3: move top n-1 disks from stack3 to stack1
            self.move_3_to_1(n - 1)

        # finished
        self.print_stacks()

    def move_2_to_3(self, n):
        # error detection
        if self._stack2.Count < n:
            raise Exception('There are no %d disks on stack2'%d, n)
        
        if n == 1:
            top = self._stack2.pop()
            if (self._stack3.Count <= 0 or top < self._stack3.peek()):
                self._stack3.push(top)
            else:
                raise Exception('Error movement of %d on %d'% (top, self._stack3.peek()))
        else: 
            # step1: move top n-1 disks from stack2 to stack1
            self.move_2_to_1(n - 1)

            # step2: move last disk from stack2 to stack3
            self.move_2_to_3(1)

            # step3: move top n-1 disks from stack1 to stack3
            self.move_1_to_3(n - 1)

        # finished
        self.print_stacks()

    def move_3_to_2(self, n):
        # error detection
        if self._stack3.Count < n:
            raise Exception('There are no %d disks on stack3'%d, n)
        
        if n == 1:
            top = self._stack3.pop()
            if (self._stack2.Count <= 0 or top < self._stack2.peek()):
                self._stack2.push(top)
            else:
                raise Exception('Error movement of %d on %d'% (top, self._stack2.peek()))
        else: 
            # step1: move top n-1 disks from stack3 to stack1
            self.move_3_to_1(n - 1)

            # step2: move last disk from stack3 to stack2
            self.move_3_to_2(1)

            # step3: move top n-1 disks from stack1 to stack2
            self.move_1_to_2(n - 1)

        # finished
        self.print_stacks()

    def move_3_to_1(self, n):
        # error detection
        if self._stack3.Count < n:
            raise Exception('There are no %d disks on stack3'%d, n)

        if n == 1:
            self.move_3_to_2(1)
            self.move_2_to_1(1)
        else:
            # step1: move top n-1 disks from stack3 to stack1
            self.move_3_to_1(n - 1)

            # step2: move last disk from stack3 to stack2
            self.move_3_to_2(1)

            # step3: move top n-1 disks from stack1 to stack3
            self.move_1_to_3(n - 1)

            # step4: move last disk from stack2 to stack1
            self.move_2_to_1(1)

            # step5: move top n-1 disks from stack3 to stack1
            self.move_3_to_1(n - 1)

        # finished
        self.print_stacks()

    def print_stacks(self):
        print '------------'
        self._stack1.print_arraystack()
        self._stack2.print_arraystack()
        self._stack3.print_arraystack()

# PROBLEM 3.5
# Implement a MyQueue class which implement by two stacks
class MyQueue(object):
    def __init__(self, max_count):
        self._max_count = max_count
        
        array1 = [0] * max_count
        array2 = [0] * max_count

        self._stack1 = ArrayStack(array1, 0, max_count)
        self._stack2 = ArrayStack(array2, 0, max_count)
        self.Count = 0

    def enqueue(self, n):
        self._dump()

        print 'enqueue', n
        if self._stack1.Count >= self._max_count:
            raise Exception('The queue is full, cannot add more items')
        else:
            self._stack1.push(n)

    def dequeue(self):
        self._dump()

        print 'dequeue'
        if self._stack2.Count == 0:
            raise Exception('There is no item in the queue')
        else:
            return self._stack2.pop()

    def peek(self):
        self._dump()

        if self._stack2.Count == 0:
            raise Exception('There is no item in the queue')
        else:
            return self._stack2.peek()

    def _dump(self):
        # when stack2 contains no items, 
        if self._stack2.Count == 0:
            while self._stack1.Count > 0:
                top = self._stack1.pop()
                self._stack2.push(top)

    def print_queue(self):
        i = self._stack2.Count - 1
        while i >= 0:
            print self._stack2._array[i],
            i -= 1

        i = 0
        while i < self._stack1.Count:
            print self._stack1._array[i],
            i += 1

        print


# PROBLEM 3.5
# use only push(), pop(), peek(), is_empty() to sort a stack in desending order
def sort_stack(stack):
    if stack.is_empty():
        return stack

    mid = stack.pop()
    if stack.is_empty():
        stack.push(mid)
        return stack

    small_array = [0] * stack._max_count
    big_array = [0] * stack._max_count
    small_stack = ArrayStack(small_array, 0, stack._max_count)
    big_stack = ArrayStack(big_array, 0, stack._max_count)

    while not stack.is_empty():
        top = stack.pop()
        if top >= mid:
            big_stack.push(top)
        else:
            small_stack.push(top)


    sorted_small_stack = sort_stack(small_stack)
    sorted_big_stack = sort_stack(big_stack)

    while not sorted_big_stack.is_empty():
        stack.push(sorted_big_stack.pop())

    stack.push(mid)

    while not sorted_small_stack.is_empty():
        stack.push(sorted_small_stack.pop())

    reverse_array = [0] * stack._max_count
    reverse_stack = ArrayStack(reverse_array, 0, stack._max_count)
    while not stack.is_empty():
        reverse_stack.push(stack.pop())
        
    return reverse_stack

        
        


# MAIN FUNCTION
if __name__ == '__main__':
    max_count = 11
    array = [0] * max_count
    stack = ArrayStack(array, 0, max_count)
    stack.push(9)
    stack.push(3)
    stack.push(7)
    stack.push(5)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(10)
    stack.push(12)
    stack.push(8)
    stack.push(6)

    stack.print_arraystack()
    sort_stack(stack).print_arraystack()
