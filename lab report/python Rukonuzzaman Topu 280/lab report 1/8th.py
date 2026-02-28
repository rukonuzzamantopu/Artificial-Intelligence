def sum_of_numbers(*args):
    total_sum = sum(args)
    return total_sum    
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(*numbers)   
print(f"The sum of the numbers {numbers} is: {result}")
