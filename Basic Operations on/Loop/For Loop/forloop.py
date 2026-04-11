#range function is used to generate a sequence of numbers. It can take one, two, or three arguments: start, stop, and step. The most common usage is with a single argument, which generates numbers from 0 up to (but not including) the specified number.

for i in range (5):
    print(i)
# Output: 0, 1, 2, 3, 4

#-----------------
#Using two arguments in range(start, stop) generates numbers from the start value up to (but not including) the stop value.

for i in range(2,5):
    print (i)

# Output: 2, 3, 4

#-----------------
#Using three arguments in range(start, stop, step) generates numbers from the start value up to (but not including) the stop value, incrementing by the step value.
for i in range(0,10,2):
    print(i)
# Output: 0, 2, 4, 6, 8

#-----------------

for i in range (10):
    print(i)
else:
    print("Loop is finished")
# Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Loop is finished

#-----------------

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

#-----------------
#loops can also be used to iterate over strings, treating each character as an element in the sequence.
for i in "orange":
    print(i)
# Output: o, r, n, a, g, e

#-----------------
fruits =["apple", "banana","cherry"]
for i in fruits:
    print(i)
    if i == "banana":
        break
# Output: apple, banana
