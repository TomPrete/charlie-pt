from random import randint
# Constraint Satisfaction Problems

# 1. Set of variables
# 2. Set of Domains, what are the possible values of the set of variables
# 3. Set of Constraints

# Strategies
# - Backtracking Search
# - Forward Checking


# variable(s) = [0,0,0,0,0,0]
# domains = [1,2,3,4,5,6,7,8,9]
# constraints
# - even indices must have an even integer
# - can't have duplicate integers in the array

# [4,5,2,7,3,9]
# [4,6,8,1,2,7]

# Example Input -> [2,3,4,5,5,6]

# checks for even index & even integer -> True or False
# Unary Constraint - only checks against a single variable
def check_idx(idx, num):
    if idx % 2 == 0:
        if num % 2 == 0:
            return True
        else:
            return False
    # if the index is odd the number can be either EVEN or ODD
    return True

# checks for duplicate values in the array -> True or False
# Higher Order Constraint - checks agains 3 or more variables within the variables
def check_duplicates(current_arr):
    non_zero_array = [num for num in current_arr if num != 0] # [2,3,4,5,7,6]
    return len(non_zero_array) == len(set(non_zero_array)) # set -> [2,3,4,5,7,6]

input = [0 for _ in range(6)]


#input = [0,0,0,0,0,0]
def csp_list_creation(input_list, current_index=0): # -> [4,3,6,8,2,9] (example solution)
    domain = [1,9]
    # base case
    if 0 not in input_list:
        return input_list
    else:
        guess = randint(*domain)
        if check_idx(current_index, guess): # replacing the current index value with the guessed number and incremting the current index by 1
            input_list[current_index] = guess
            current_index += 1
            if not check_duplicates(input_list): # if there are repeating numbers in the input list go back and replace the value at the previous index back to 0
                current_index -= 1
                input_list[current_index] = 0
        return csp_list_creation(input_list, current_index)

print(csp_list_creation([0 for _ in range(6)]))
