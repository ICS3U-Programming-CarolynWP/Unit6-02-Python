# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/15
# Generates 10 random numbers then uses a function
# To calculate the number with the highest value.
# Displays it to user.

import random

# Function to find the maximum value
def find_max_value(list_of_int):
    # Variables
    max_number = -1
    counter = 0

    # For loop to determine the max number
    for counter in range(10):
        current_number = list_of_int[counter]
        if current_number > max_number:
            max_number = current_number

    # Returning the calculation back to main()
    return max_number


def main():
    # Variables
    list_of_integers = []
    counter = 0
    MIN_NUM = 0
    MAX_NUM = 100
    MAX_LIST_SIZE = 10

    # To generate the random numbers and add them to the list
    for counter in range(0, MAX_LIST_SIZE):
        random_number = random.randint(MIN_NUM, MAX_NUM)
        list_of_integers.append(random_number)
        print("{} added to the list ".format(list_of_integers[counter]))

    # To call the function and display the maximum value
    max = find_max_value(list_of_integers)
    print("The highest number is {} ".format(max))


if __name__ == "__main__":
    main()
