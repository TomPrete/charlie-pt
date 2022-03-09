# How to create an individual Node
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    # Helper to insert node
    def insert_node(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find_smallest(self, current_node):
        # self.current_node
        pass


# 10 -> 5 -> 1 (smallest node)
