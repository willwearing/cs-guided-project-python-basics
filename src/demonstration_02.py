"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    # Your code here
    """
    Input: int
    Output: int

    We know there are 60 seconds in a minute 
    Given n minutes, we can convert that into seconds with the formula: n*60

    """

    # short version - return minutes * 60

   answer = minutes * 60
   return answer

convert(10)