# comments
name = 'Tom'
age = 32

# if age > 21:
#     print(f"You are {age} years old, You can come into the bar") # string interpolation
# elif age == 18:
#     print('You can vote')
#     print('You can vote')
# else:
#     print('Go Away')

fruits = ['apples', 'banana', 'watermellon', 'cherry']

# print(len(fruits))
# For loops
# for i in range(31, 0, -2):
#     print(i)


# for i in range(len(fruits)):
#     print(fruits[i])

# For...in (LIST)
# for fruit in fruits:
#     if fruit == 'cherry':
#         print(f'{fruit} is my favorite')
#     else:
#         print(fruit)

# (ENUMERATE method)
# for idx, fruit in enumerate(fruits):
#     print(idx, fruit)

obj = {
  'age': 31,
  'name': 'Tom',
  'hobbies': ['reading', 'working out', 'sleeping']
}


def print_obj_values(some_object):
    for key in some_object:
        print(f"Key: {key} - Value: {some_object[key]}")

# printObjValues(obj)
