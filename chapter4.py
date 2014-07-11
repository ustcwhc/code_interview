#!/usr/bin/python
# filename: chapter4.py


# TREE CLASS
class Tree(object):
    def __init__(self, n):
        self.Parent = None
        self.LeftChild = None
        self.RightChild = None
        self.Data = n

    def insert(self, node):
        # go to left
        if self.Data >= node.Data:
            if not self.LeftChild:
                self.LeftChild = node
                node.Parent = self
            else:
                self.LeftChild.insert(node)
        # got right
        else:
            if not self.RightChild:
                self.RightChild = node
                node.Parent = self
            else:
                self.RightChild.insert(node)

    def find(self, data):
        print 'finding', data
        # bingo
        if self.Data == data:
            return self
        # go to left
        elif self.Data > data:
            if not self.LeftChild:
                print 'not found'
                return None
            else:
                return self.LeftChild.find(data)
        # go to right
        else:
            if not self.RightChild:
                print 'not found'
                return None
            else:
                return self.RightChild.find(data)

    def _find_leftmost(self):
        node = self
        while node.LeftChild:
            node = node.LeftChild
        return node

    def find_rightmost(self):
        node = self
        while node.RightChild:
            node = node.RightChild
        return node

    def delete(self, node):
        print
        print 'delete', node.Data

        # get left or right: -1-root, 0-left, 1-right
        if not node.Parent:
            left_or_right = -1
        elif node == node.Parent.LeftChild:
            left_or_right = 0
        else:
            left_or_right = 1

        # single node: directly delete
        if not node.LeftChild and not node.RightChild:
            if left_or_right < 0:
                return None
            elif left_or_right == 0:
                node.Parent.LeftChild = None
                return node.Parent.get_root()
            else:
                node.Parent.RightChild = None
                return node.Parent.get_root()
        else:
            # only has left child: connect child to parent
            if not node.RightChild:
                if left_or_right == 0:
                    node.Parent.LeftChild = node.LeftChild
                elif left_or_right > 0:
                    node.Parent.RightChild = node.LeftChild
                node.LeftChild.Parent = node.Parent
                return node.LeftChild.get_root()

            # only has right child: connect child to parent
            elif not node.LeftChild:
                if left_or_right == 0:
                    node.Parent.LeftChild = node.RightChild
                elif left_or_right > 0:
                    node.Parent.RightChild = node.RightChild
                node.RightChild.Parent = node.Parent
                return node.RightChild.get_root()

            # has both left and right children: replace by left-rightmost node
            else:
                left_rightmost_node = node.LeftChild.find_rightmost()
                if node.LeftChild == left_rightmost_node:
                    if left_or_right == 0:
                        node.Parent.LeftChild = node.LeftChild
                    elif left_or_right > 0:
                        node.Parent.RightChild = node.LeftChild
                    node.LeftChild.RightChild = node.RightChild
                    node.LeftChild.Parent = node.Parent
                    return node.LeftChild.get_root()
                else:
                    node.Data = left_rightmost_node.Data
                    return self.delete(left_rightmost_node)

    def get_root(self):
        node = self
        while node.Parent:
            node = node.Parent
        return node

    def print_tree(self):
        if not self.Parent:
            head = 'T'
        elif self.Parent.LeftChild == self:
            head = 'L'
        else:
            head = 'R'

        print '(' + head, self.Data,
        if self.LeftChild:
            self.LeftChild.print_tree()
        if self.RightChild:
            self.RightChild.print_tree()
        print ')',


# ENUM CLASS
class VisitStates:
    UnVisited = '0'
    Visited = '1'


# GRAPH CLASS
class GraphNode(object):
    def __init__(self, data):
        self.Data = data
        self.Neighbors = []
        self.VisitState = VisitStates.UnVisited


# PROBLEM 4.1
# check whether a tree is balanced
### return the depth of the tree
### leaf return 1
### not balanced return -1
def get_balance_dept(tree):
    if not tree:
        return 0
    else:
        left_dept = get_balance_dept(tree.LeftChild)
        if left_dept < 0:
            return -1

        right_dept = get_balance_dept(tree.RightChild)
        if right_dept < 0:
            return -1

        if abs(left_dept - right_dept) > 1:
            return -1

        return max(left_dept, right_dept) + 1 


# PROBLEM 4.2
# check whether two nodes has a route in a graph
def has_route(all_nodes, start, end):
    if start == end:
        return True

    for node in all_nodes:
        node.VisitState = VisitStates.UnVisited

    queue = {}
    queue.append(start)

    while len(queue) > 0:
        node = queue.pop(0)
        for neighbor in node.Neighbors:
            if neighbor.VisitState == VisitStates.UnVisited:
                # found
                if neighbor == end:
                    return True
                else:
                    neighbor.VisitState = VisitStates.Visited
                    queue.append(neighbor)

    # not found
    return False


# PROBLEM 4.3
# Given an ascending array, create a binary tree with minimum height
def create_tree_with_asc(asc_array):
    length = len(asc_array)
    index_double_queue = {}
    start = 0
    end = length - 1
    if 1 > 3:
        pass

# MAIN FUNCTION
if __name__ == '__main__':
    root6 = Tree(6)
    node4 = Tree(4)
    node8 = Tree(8)
    node2 = Tree(2)
    node5 = Tree(5)
    node7 = Tree(7)
    node9 = Tree(9)

    root6.insert(node4)
    root6.insert(node8)
    root6.insert(node2)
    root6.insert(node5)
    root6.insert(node7)
    root6.insert(node9)

    root6.print_tree()
    print get_balance_dept(root6)
    
    root6.delete(root6).print_tree()
    print get_balance_dept(root6)

    root6.delete(node2).print_tree()
    print get_balance_dept(root6)
    
    root6.delete(node4).print_tree()
    print get_balance_dept(root6)
