class Person:
    num_of_eyes = 2 # class variable

    # Automatically called when creating a new instance of a Person
    def __init__(self, name, occupation, age=20):
        self.name = name # instance variables
        self.age = age
        self.occupation = occupation

    # Instance Method -> can call/invoke them on each individual instance of the class
    def eat(self):
        return 'nom nom nom!'

    def increase_age(self, years_increased):
        random_num = 10 # local variable
        self.age = self.age + years_increased
        return f"My new age is {self.age}"

    def print_my_age(self):
        return f"My age is {self.age}"

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation

    def change_num_of_eyes(self):
        Person.num_of_eyes = 3

    def make_pirate(self):
        self.num_of_eyes = 1



tressa  = Person('Tressa', 'Software Engineer')
william = Person('William','Software Developer', 23)
pirate = Person('Jack SParrow', 'Pirate', 40)

print(william.num_of_eyes)
print(tressa.num_of_eyes)
tressa.change_num_of_eyes()
print(william.num_of_eyes)
print(tressa.num_of_eyes)
pirate.make_pirate()
print(pirate.num_of_eyes)


# print(tressa.eat())
# print(tressa.print_my_age())
# print(tressa.increase_age(2))
# tressa.change_occupation('Principle Software Engineer')

