"""
Task 1

Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""

def solution(A):

    #convert array into a set for quick look ups
    integer_set = set(A)
    lowest_positive_integer = 1

    # while current lowest_positive_integer is in integer_set, keep incrementing it until it's not present in integer_set
    while lowest_positive_integer in integer_set:
        lowest_positive_integer += 1
    

    return lowest_positive_integer
