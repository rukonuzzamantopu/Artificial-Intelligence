numbers = [1, -2, 3, 0, -5, 6]
positive_count = 0
negative_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
zero_count = len(numbers) - positive_count - negative_count
print(f"Zeroes: {zero_count}")
