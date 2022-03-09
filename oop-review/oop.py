# from leaf_file import Leaf

import random

class Tree:
    has_bark = True #class variable -> same value across all instance of Tree

    def __init__(self, is_deciduous):
        self.is_deciduous = is_deciduous # value is unique to each instance of the Tree class
        self.age = 0 # instance variables (prepending the 'self' keyword on the variable)

    #instance method
    def age_tree(self):
        self.age += 1
        return self.age

    #instance method
    # def change_bark(self):
    #     Tree.has_bark = False # changes class variable value and is reflected across all instances

    # Methods that you can execute only on the Class (not an instance of a class)
    @classmethod #decorator
    def change_bark(cls):
        cls.has_bark = False # changes class variable value and is reflected across all instances


# ----- Inheritance (is-a relationship)

class Oak(Tree): # Oak is a Tree

    def __init__(self, is_deciduous, wood_type, has_acorns=False):
        super().__init__(is_deciduous)
        self.wood_type = wood_type
        self.has_acorns = has_acorns
        self.height = 0
        self.leaves = []

    def age_tree(self, to_produce_acorns=False):
        if to_produce_acorns:
            self.age = 20
            self.has_acorns = True
            self.height = self.age * 3
        else:
            self.age += 1
            self.height += 3
            if self.height >= 3:
                self.create_leaves()
        return self.age

    def create_leaves(self):
        random_num_of_leaves = random.randint(1,10)
        for i in range(random_num_of_leaves):
            self.leaves.append(Leaf('narrow', 'green', random.randint(1,3))) # has-a relationship (Oak has-a leaf(leaves))

    def leaf_count(self):
        print(self.leaves)
        return len(self.leaves)

    def view_leaf_attributes(self):
        for leaf in self.leaves:
            print(leaf)


# ---- Composition (has-a relationship)
class Leaf:

    def __init__(self, type, color, size):
        self.type = type
        self.color = color
        self.size = size

    def __str__(self):
        return f"""
            Type: {self.type}
            Color: {self.color}
            Size: {self.size}
        """



oak_1 = Oak(True, 'hard', False)

print(oak_1.leaf_count())
oak_1.age_tree()
print(oak_1.age)
print(oak_1.height)
print(oak_1.leaf_count())
print(oak_1.view_leaf_attributes())
