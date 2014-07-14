#!/usr/bin/python
# filename: chapter4.py


# TREE CLASS
class Tree(object):
    def __init__(self, n):
        self.Parent = None
        self.LeftChild = None
        self.RightChild = None
        self.Data = n
        self.VisitState = VisitStates.UnVisited

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

    queue = []
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
    left_right_queue = []
    root = None
    left_right_queue.append((0, length - 1))
    while len(left_right_queue) > 0:
        top = left_right_queue.pop(0)
        if top[0] <= top[1]:
            mid = (top[0] + top[1]) / 2
            if not root:
                root = Tree(asc_array[mid])
            else:
                root.insert(Tree(asc_array[mid]))

            # append left and right
            left_right_queue.append((top[0], mid - 1))
            left_right_queue.append((mid + 1, top[1]))

    return root


# PROBLEM 4.4
# given a binary search tree, design an algorithm to create a binary tree
# which creats a linked list of all the nodes at each depth
def get_list_of_depth(tree):
    lists=[]
    data_lists=[]
    lists.append([tree])
    data_lists.append([tree.Data])
    while True:
        list = []
        for node in lists[len(lists) - 1]:
            if node.LeftChild:
                list.append(node.LeftChild)
            if node.RightChild:
                list.append(node.RightChild)

        if len(list) > 0:
            lists.append(list)
            data_lists.append([node.Data for node in list])
        else:
            break
    return data_lists


# PROBLEM 4.5
# Write an algorithm to find the 'next' node (i.e. in-order successor) of
# a given node in a binary search tree where each node has a link to its parents
def get_next_node(node):
    print 'Next node of ' + str(node.Data) + 'is ',
    if node.LeftChild:
        return node.LeftChild
    elif node.RightChild:
        return node.RightChild
    else:
        parent = node.Parent
        while (parent and
                   (not parent.RightChild or
                       parent.RightChild == node)
                ):
            node = parent
            parent = parent.Parent
        if parent:
            return parent.RightChild
        else:
            return None


# PROBLEM 4.6
# Find the first common ancestor of two nodes.
# Avoid storing additional nodes in data structure
def get_common_ancestor(root, node1, node2):
    if is_cover(root.LeftChild, node1) and is_cover(root.LeftChild, node2):
        return get_common_ancestor(root.LeftChild, node1, node2)
    elif is_cover(root.RightChild, node1) and is_cover((root.LeftChild, node2)):
        return get_common_ancestor(root.RightChild, node1, node2)
    else:
        return root

def is_cover(root, node):
    if not root:
        return False

    if root == node:
        return True

    is_covered = False
    if root.LeftChild:
        is_covered = is_cover(root.LeftChild, node)
    if not is_covered and root.RightChild:
        is_covered = is_cover(root.RightChild, node)
    return is_covered


# PROBLEM 4.7
# Design algorithm to decide whether a small tree is a
# subtree of a very large tree
def is_sub_tree(small_tree, large_tree):
    if not small_tree:
        return True

    if not large_tree:
        return False

    if small_tree.Data == large_tree.Data:
        return match_tree(small_tree, large_tree)
    else:
        return is_sub_tree(small_tree, large_tree.LeftChild) or \
                is_sub_tree(small_tree, large_tree.RightChild)

def match_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if not tree1 or not tree2:
        return False

    if tree1.Data != tree2.Data:
        return False

    return match_tree(tree1.LeftChild, tree2.LeftChild) and \
            match_tree(tree1.RightChild, tree2.RightChild)



# PROBLEM
# MAIN FUNCTION
if __name__ == '__main__':
    asc_array = [i for i in range(10)]
    tree = create_tree_with_asc(asc_array)
    tree.print_tree()
    print get_next_node(tree.find(0)).Data
    print get_next_node(tree.find(1)).Data
    print get_next_node(tree.find(2)).Data
    print get_next_node(tree.find(3)).Data
    print get_next_node(tree.find(4)).Data
    print get_next_node(tree.find(5)).Data
    print get_next_node(tree.find(6)).Data
    print get_next_node(tree.find(8)).Data
    print get_next_node(tree.find(9)).Data
