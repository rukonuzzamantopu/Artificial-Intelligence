"""Membership operators demonstration

This module demonstrates Python's membership operators:
- ``in``: returns True if a value is a member of a sequence or collection
- ``not in``: returns True if a value is not a member

Use `in` for membership tests (lists, tuples, sets, strings, dict keys, etc.).
"""

# Examples with lists and tuples
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits ->", "apple" in fruits)       # True
print("'pear' in fruits ->", "pear" in fruits)         # False
print("'pear' not in fruits ->", "pear" not in fruits) # True

nums = (1, 2, 3, 4)
print("2 in nums ->", 2 in nums)   # True

# Strings (substring membership)
text = "hello world"
print("'hello' in text ->", "hello" in text)   # True
print("'ow' in text ->", "ow" in text)         # True (substring)

# Sets (membership is O(1) average)
letters = set(["a", "b", "c"]) 
print("'b' in letters ->", 'b' in letters)      # True

# Dictionaries: membership tests keys only
person = {"name": "Alice", "age": 30}
print("'name' in person ->", 'name' in person)   # True
print("'Alice' in person ->", 'Alice' in person) # False (value, not key)

# Membership with custom objects: implement __contains__ or iterate
class Bag:
	def __init__(self, items):
		self._items = list(items)
	def __contains__(self, item):
		return item in self._items

bag = Bag(["pen", "notebook"])
print("'pen' in bag ->", 'pen' in bag)   # True

# Notes: prefer `==` for value equality; `in` checks membership semantics.



