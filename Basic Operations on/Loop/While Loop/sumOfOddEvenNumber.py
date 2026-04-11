i = 1
sum_odd = 0
sum_even = 0
while i <= 10:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    i += 1
print("Sum of odd numbers between 1 and 10:", sum_odd)
print("Sum of even numbers between 1 and 10:", sum_even)