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

# PROBLEM 2.1
# Delete the duplicate nodes when the list is unsorted
    def delete_duplicate(self):
        # count the data frequency
        data_dic = {}
        node = self
        while node:
            if data_dic.has_key(node.Data):
                data_dic[node.Data] += 1
            else:
                data_dic[node.Data] = 1
            node = node.Next
        # delete duplicate until the frequency is 1
        head = self
        cur_node = self
        parent_node = None
        while cur_node:
            # delete
            if data_dic[cur_node.Data] > 1:
                data_dic[cur_node.Data] -= 1
                cur_node = cur_node.Next

                if parent_node:
                    parent_node.Next = cur_node
                else:
                    head = cur_node
                    parent_node = head
                
            else:
                parent_node = cur_node
                cur_node = cur_node.Next
        
        return head

# PROBLEM 2.2
# Find the nth to last element of a singly linked list
    def get_last_nth_node(self, n):
        # get list length
        length = 0
        cur_node = self
        while cur_node:
            length += 1
            cur_node = cur_node.Next
        print 'list length', length
        # get target index
        if n >= length:
            print 'n(%d) is not smaller than list length(%d)'% (n, length)
            return None
        target = length - n - 1
        index = 0
        cur_node = self
        while cur_node:
            if index == target:
                return cur_node
            index += 1
            cur_node = cur_node.Next
        return None

# PROBLEM 2.3
# Delete a node in a singly linked list, you can only access that node, and you cannot access other nodes
    def delete(self):
        if not self or not self.Next:
            return False
        self.Data = self.Next.Data
        self.Next = self.Next.Next

# PROBLEM 2.4
# You have two numbers representend by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
    def digit_add(list1, list2, cur_digit):
        if not list1 and not list2:
            return None

        value = cur_digit
        if list1:
            value += list1.Data
        if list2:
            value += list2.Data

        next_digit = value % 10
        result = Node(next_digit)
        next_node = None

        if list1 and list1.Next:
            next_node = list1.Next.digit_add(list2.Next, value / 10)
        elif list2 and list2.Next:
            next_node = list2.Next.digit_add(None, value / 10)
        
        result.append(next_node)
        return result

# PROBLEM 2.5
# Find the start of a loop for a given list
    def find_loop_start(self):
        '''Version 1: use dictionary method'''
        node_dic = {}
        cur_node = self
        while cur_node:
            if node_dic.has_key(cur_node):
                return cur_node
            node_dic[cur_node] = 1
            cur_node = cur_node.Next
        return None
    def find_loop_start_no_dic(self):
        '''Version 2: not use dictionary method'''
        # two person run from the beginning, p2 is twice faster than p1
        p1 = self;
        p2 = self;

        # break when they meet
        while p2 and p2.Next:
            p1 = p1.Next
            p2 = p2.Next.Next
            if(p1 == p2):
                break

        # there is no loop
        if not p2 or not p2.Next:
            print 'There is no loop'
            return None

        # p2 run again, when they meet, the position is the start point
        p2 = self
        while p1 != p2:
            p1 = p1.Next
            p2 = p2.Next

        return p1

# MAIN FUNCTION
if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(1)
    node3 = Node(5)
    node4 = Node(5)
    node5 = Node(9)
    node6 = Node(2)

    node1.append(node2)
    node2.append(node3)
    node3.append(node4)
    node4.append(node5)
    node5.append(node6)
    node6.append(node2)

    loop_start = node1.find_loop_start_no_dic()
    if loop_start:
        print loop_start.Data
    else:
        print 'There is no loop'
