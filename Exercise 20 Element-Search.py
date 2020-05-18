# Exercise 20 (and Solution)
#
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
# to largest) and another number. The function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import random


def random_sorted_list():
    random_list = [random.randrange(1, 999) for i in range(10)]
    random_list.sort()
    return random_list


def search_num(a, b):
    if a in b:
        return True
    else:
        return False


check_list = random_sorted_list()
print(check_list)

print("I will ask you for a number and then check if that number is in a randomly generated list.")
user_num = int(input("Please, enter a number: "))

print(search_num(user_num, check_list))
