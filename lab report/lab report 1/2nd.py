numbers = [10, 8, 9, 7, 5, 6]
smallest = numbers[0]   
for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)
