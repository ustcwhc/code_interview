#!/usr/bin/python
# filename: chapter4.py

# CLASS
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

    def _find_rightmost(self):
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
                left_rightmost_node = node.LeftChild._find_rightmost()
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


# MAIN FUNCTION
if __name__ == '__main__':
    root6 = Tree(6)
    node4 = Tree(4)
    node8 = Tree(8)
    node2 = Tree(2)
    node5 = Tree(5)
    node45 = Tree(4.5)
    node46 = Tree(4.6)
    node7 = Tree(7)
    node9 = Tree(9)

    root6.insert(node4)
    root6.insert(node8)
    root6.insert(node2)
    root6.insert(node5)
    root6.insert(node45)
    root6.insert(node46)
    root6.insert(node7)
    root6.insert(node9)
    root6.print_tree()

    root6.delete(root6).print_tree()
    root6.delete(root6).print_tree()

    print
    root6.find(6).print_tree() 
