# def times_two(num):
#     return num * 2

# let times_two = num => num * 2
times_two = lambda num: num * 2
# print(times_two(6))

# Lambda's with multiple parameters
multiply = lambda num_1, num_2: num_1 * num_2
# print(multiply(3,5))

arr_of_nums = [1,53,6,3,6,643,4,6,73,4,7,86,34,45,7,4,5]

odd_nums = list(filter(lambda num: num % 2 != 0, arr_of_nums))
# print(odd_nums)

double_num_list = list(map(lambda num: num * 2, arr_of_nums))
print(double_num_list)

