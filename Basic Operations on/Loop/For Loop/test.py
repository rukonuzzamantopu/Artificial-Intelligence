# Program to find sum of numbers between 50 and 100
# divisible by 3 and not divisible by 5

total_sum = 0

for i in range(50, 101):
    if i % 3 == 0 and i % 5 != 0:
        total_sum += i

print("Sum of numbers divisible by 3 and not divisible by 5 is:", total_sum)

#output:
#Sum of numbers divisible by 3 and not divisible by 5 is: 1050