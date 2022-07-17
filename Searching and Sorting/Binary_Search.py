"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(input_array)-1

    # while you havent narrowed it down to one element...
    while low <= high:
        # ...check the middle element
        mid = (low + high)
        guess = input_array[mid]
        # found the element
        if guess == value:
            return mid
        # the guess was too high
        if guess > value:
            high = mid - 1
        # the guess was too low
        else:
            low = mid + 1
    # the item doesn't exist
    return -1


# Let's test it!
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
