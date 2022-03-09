# name = 'Tom'
# age = 35

# info = {
#     name: 'Julie',
#     age: 35,
# }

# fruits = ['apples']

# print(type(name))
# print(type(age))
# print(type(info))
# print(type(fruits))

# This Dog Class is a blueprint to creating new instance of a Dog object
class Dog:

    def __init__(self, name):
        # instance variables (with the self keyword)
        self.num_of_legs = 4
        self.name = name

    def print_legs(self):
        return f"{self.name} has {self.num_of_legs} legs"

    def update_legs(self, new_leg_count):
        self.fda = new_leg_count
        return self.fda




dog1 = Dog('Sadie')
dog2 = Dog('Rosie')
# dog3 = Dog()

print(dog1.print_legs())
print(dog1.update_legs(3))
print(dog1.print_legs())

# print(dog2)
# print(dog2.num_of_legs)
# print(dog2.name)
# print(type(dog3))


