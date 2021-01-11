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
​
    """
    def find_len(string):
        return len(string)
​
    lst.sort(key=find_len)
    """
​
    """
    lst.sort(key=len)
    """
​
    lst.sort(key=lambda string: len(string))
    return lst
​
​
print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))