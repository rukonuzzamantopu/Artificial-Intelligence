numbers = [10, 8, 9, 7, 5, 6]
largest = float('-inf') 
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)
