"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    """
    Input: list of unsorted ints
    Output: int, the nth smallest int in the list

    If in the input is sorted in ascending order, we can then simply 
    return the nth element from our sorted list

    1.sort the list in ascending order 
    2. return the nth list element
    """
    #check and handle index-out-of-range issues, lets check to make
    #sure that n <= len(lst)
    if n <= len(lst) and n > 0:
        #sort the list of numbers in ascending order
        lst.sort()
        #return the nth list element
        return lst[n - 1]
    
    return None

print(nth_smallest([1, 3, 5, 7], 1))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([1, 3, 5, 7], 0))