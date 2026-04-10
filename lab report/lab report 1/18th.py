numbers = [10, 8, 9, 7, 5, 6]
largest = float('-inf')
smallest = float('inf')
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
difference = largest - smallest
print("The difference between the largest and smallest numbers is:", difference)

