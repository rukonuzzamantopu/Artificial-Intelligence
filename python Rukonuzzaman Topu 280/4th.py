numbers = [10, 8, 9, 7, 5, 6]
largest = float('-inf')
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num
print("The second-highest number is:", second_largest)