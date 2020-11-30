"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    """
    Input: int
    Output: int

    The length and width inputs correspond to a rectangle 
    Perimeter: the distance around the entire rectangle
    length * 2 + width * 2

    What about negative integers? If at least one of our parameters is negative, we'll return 0
    Do negative distances make sense? 
    """

    
    if length < 0 or width < 0:
        return 0
    #return length * 2 + width * 2
    answer = length * 2 + width * 2
    return answer
    
print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9))
print(find_perimeter(-2, 20))
