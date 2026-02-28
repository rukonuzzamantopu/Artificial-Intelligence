def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = 10
result = check_even_odd(number)
print(f"The number {number} is {result}.")
