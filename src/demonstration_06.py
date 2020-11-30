"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    """
    Input: string that may or may not contain x's or o's
    Output: boolean indicating whether the string has the same number of x's or o's

    Casing doesn't matter, treat capital and lowercase x's and o's are the same

    When we walked through the examples ourselves, we essentially counted the number of x's and o's

    If the number of x's and o's matched, return true, otherwise if they differ, we return false

    """

    num_xs = 0
    num_os = 0
    
    for letter in txt.lower():
        if letter == 'x':
            num_xs += 1
        # this does not need to be an elif (else if) because 
        # we're never going to get a letter that is both an x and an o
        if letter == 'o':
            num_os += 1
   
    return num_xs == num_os

print(XO("ooxx"))
print(XO("xooxx")) 
print(XO("ooxXm"))
print(XO("zpzpzpp")) 
print(XO("zzoo"))