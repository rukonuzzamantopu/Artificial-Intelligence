# Program to find second highest number without sorted()

numbers = {12, 45, 7, 23, 56, 89, 34}

highest = second_highest = -float('inf')

for num in numbers:
    if num > highest:
        second_highest = highest
        highest = num
    elif num > second_highest and num != highest:
        second_highest = num

print("Numbers:", numbers)
print("Second highest number is:", second_highest)

#output:
#Numbers: {34, 45, 7, 12, 56, 89, 23}
#Second highest number is: 56