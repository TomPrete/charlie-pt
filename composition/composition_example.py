class Animal:
    def __init__(self, diet, weight):
        self.diet = diet
        self.weight = weight

# Mammal is-an Animal
class Mammal(Animal):
    def __init__(self, is_primate, diet, weight):
        super().__init__(diet, weight)
        self.is_primate = is_primate

# Dog is-a Mammal
class Dog(Mammal):
    def __init__(self, name, breed, is_primate, diet, weight, paw_color, has_dewclaw):
        super().__init__(is_primate, diet, weight)
        self.name = name
        self.breed = breed
        self.paws = Paw(paw_color, has_dewclaw) #Composition (Dog HAS-A Paw) NOT Dog is-a Paw or Paw is-a Dog

    def __str__(self):
        return f"""
            Name: {self.name}
            Breed: {self.breed}
            Is Primate: {self.is_primate}
            Diet: {self.diet}
            Weight: {self.weight}
            Paws: {self.paws}
        """

class Paw:
    def __init__(self, paw_color, has_dewclaw):
        self.paw_color = paw_color
        self.has_dewclaw = has_dewclaw

    def __str__(self):
        return f"Paw Color: {self.paw_color} - Has Dewclaw: {self.has_dewclaw}"

    def print_attributes(self):
        return f"(Instance Method in Paw Object) Paw Color: {self.paw_color} - Has Dewclaw: {self.has_dewclaw}"

# Inheritance is an 'IS-A' relationship
# Composition is a 'HAS-A' relationship
# lucy = Dog('Lucy', 'Golden Retreiver', False, 'Primarily Carnivor', 60, 'red', True)
# print(lucy.paws.print_attributes())

# Robot HAS-A Head
# Robot HAS-A Body
# Robot HAS-A Leg(s)
class Robot:
    def __init__(self, head_type, body_size, num_of_legs):
        self.head = Head(head_type)
        self.body = Body(body_size)
        self.legs = Leg(num_of_legs)

class Body:
    def __init__(self, size):
        self.size = size

class Leg:
    def __init__(self, num_of_legs):
        self.num_of_legs = num_of_legs

class Head:
    def __init__(self, type_of_head):
        self.type_of_head = type_of_head

    def display_head_type(self):
        return f"Head Type: {self.type_of_head}"


robot_1 = Robot('Square', 'Huge', 4)
print(robot_1.body)
print(robot_1.head.display_head_type())
print(robot_1.legs)
