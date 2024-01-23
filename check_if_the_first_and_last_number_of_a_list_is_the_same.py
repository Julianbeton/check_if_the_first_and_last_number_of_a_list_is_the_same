# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given:
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# Expected Output:
# Given list: [10, 20, 30, 40, 10]
# result is True
# numbers_y = [75, 65, 35, 75, 30]
# result is False

def checking_if_the_first_and_last_number_is_equal(given_list):
    
    first_number = given_list[0]
    last_number = given_list[4]

    if first_number / last_number == 1:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("\033[1;32;40m", numbers_x,"The result in number_x given is", checking_if_the_first_and_last_number_is_equal(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("\033[1;32;40m", numbers_y,"The result in number_x given is", checking_if_the_first_and_last_number_is_equal(numbers_y))
