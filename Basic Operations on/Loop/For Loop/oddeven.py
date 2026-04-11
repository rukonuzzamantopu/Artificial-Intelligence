""" for i in range (100):
    if i%2 ==0:
        print(i,"is even")
    else:
        print(i,"is odd")

 """
even = 0
odd = 0

for i in range(100):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Sum of even numbers is", even)
print("Sum of odd numbers is", odd)
        
#output:
#Sum of even numbers is 2450
#Sum of odd numbers is 2500

#
# Program to find sum of odd and even numbers from a set

# Create a set of numbers
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

even_sum = 0
odd_sum = 0

# Loop through each number in the set
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Display results
print("Numbers in the set:", numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)



