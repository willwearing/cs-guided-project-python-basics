"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    """
    Input: list of strings, where all strings are possibly a different length
    Output: list of strings, where the strings are sorted by length in ascending order

    If we're given an empty list, return an empty list

    What does sorted by length in ascending order mean? It means that it sorts by string length

    If two strings have the same length, sort those in alphabetical order
    """
    # lst.sort(key=len)
    lst.sort(key=lambda x: (len(x), x))
    return lst

print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length([]))
print(sort_by_length(["apple", "pie", "shortcake"]))