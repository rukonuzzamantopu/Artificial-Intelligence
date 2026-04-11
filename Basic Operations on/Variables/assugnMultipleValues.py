#Python allows you to assign values to multiple variables in one line:
x,y,z="topu","ashab","modu"

print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
a=b=c=10
print(a)
print(b)
print(c)

#If you have a collection of values in a list, tuple, etc. Python allows you to extract the values into variables.
#This is called unpacking.

fruits=["apple ","banana ","cherry "]
x,y,z=fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
print(x,y,z)

#You can also use the + operator to output multiple variables:
print(x + y + z)

#For numbers, the + character works as a mathematical operator:
a=5
b=10
print(a+b)
