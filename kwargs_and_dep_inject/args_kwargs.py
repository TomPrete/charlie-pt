def add_up_to(num_1, num_2, *nums):
    answer = num_1 + num_2
    if len(nums) > 0:
        for num in nums:
            answer += num
    return answer

# print(add_up_to(1,4,6,7,89,4))

# Kwarg -> Key word arguments
tom = {
    'name': 'Tom Prete',
    'age': 35,
    'occupation': 'software developer'
}

sarah = {
    'name': 'Sarah',
    'age': 35,
    'occupation': 'software developer',
    'more_keys': 'do somethign with this'
}

def get_employee_info(*args, **kwargs): #-> name='Tom Prete', age=35, occupation='software developer'
    for key in kwargs:
        print(key)
    for value in kwargs.values():
        print(value)
    for item in kwargs.items():
        print(f'{item[0]}: {item[1]}')


# print(get_employee_info(**tom))


class Employee:

    def __init__(self, **employee_info):
        self.name = employee_info['name']
        self.age = employee_info['age']
        self.occupation = employee_info['occupation']

emp_1 = Employee(**sarah)
emp_2 = Employee(**tom)
# print(dir(emp_1))
# print(dir(emp_2))
