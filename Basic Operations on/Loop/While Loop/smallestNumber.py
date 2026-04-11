# Program to find smallest number from a set using while loop

numbers = {12, 45, 7, 23, 56, 3, 89}

# Convert set to list (because while loop needs indexing)
num_list = list(numbers)

smallest = num_list[0]

i = 1
while i < len(num_list):
    if num_list[i] < smallest:
        smallest = num_list[i]
    i += 1

print("Numbers:", numbers)
print("Smallest number is:", smallest)

# Output:
# Numbers: {3, 7, 12, 23, 45, 56, 89}
# Smallest number is: 3