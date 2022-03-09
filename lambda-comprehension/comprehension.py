def create_list():
    some_list = []
    for i in range(10):
        some_list.append(i)
    return some_list

# print(create_list())

# [expression for item in iterable_item]
list_1 = [i for i in range(10)]
# print(list_1)

arr_of_nums = [1,53,6,3,6,643,4,6,73,4,7,86,34,45,7,4,5]
# double_num_list = list(map(lambda num: num * 2, arr_of_nums))
# print(double_num_list)

# double_num_list = [num * 2 for num in arr_of_nums]
# print(double_num_list)

# odd_nums = list(filter(lambda num: num % 2 != 0, arr_of_nums))
# print(odd_nums)

#Conditional (if statement) - single "if statement"
odd_nums = [num for num in arr_of_nums if num % 2 != 0]
# print(odd_nums)

#
odd_even_index = [num * 2 if num % 2 == 0 else num - 5 for num in arr_of_nums]
print(odd_even_index)




