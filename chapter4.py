#!/usr/bin/python
# filename: chapter4.py

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
        # bingo
        if self.Data == data:
            return self
        # go to left
        elif self.Data > data:
            if not self.LeftChild:
                return None
            else:
                return self.LeftChild.find(data)
        # go to right
        else:
            if not self.RightChild:
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
        # get left or right: -1-root, 0-left, 1-right
        if not node.Parent:
            left_or_right = -1
        elif node == node.Parent.LeftChild:
            left_or_right = 0
        else:
            left_or_right = 1

        # single node: directly delete
        if not node.LeftChild and not node.LeftChild:
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
                left_rightmost_node = _find_rightmost(node.LeftChild)
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
                    return self.delete(left_rightmost_node, left_rightmost_node)
                

    def get_root(self):
        node = self
        while node.Parent:
            node = node.Parent
        return node

