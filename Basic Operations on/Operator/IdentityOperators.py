""" Identity operators
Identity operators are used to compare the memory locations of two objects. The two main identity operators in
Python are:
• is: Returns True if both operands refer to the same object
• is not: Returns True if both operands do not refer to the same object """
# Example of identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # Output: True
print(a is c)  # Output: False
print(a == c)  # Output: True

""" Identity operators with immutable types
In this code snippet, we demonstrate the behavior of identity operators with immutable types like integers and strings. For small integers (between -5 and 256), Python reuses the same memory location, so 'is' returns True. However, for larger integers and strings, Python creates new objects, resulting in 'is' returning False, even if the values are the same. """
x = 10  
y = 10
print(x is y)  # Output: True
x = 1000
y = 1000
print(x is y)  # Output: False
a = "Hello"
b = "Hello"
print(a is b)  # Output: True

a = "Hello, World!"
b = "Hello, World!"
print(a is b)  # Output: False

