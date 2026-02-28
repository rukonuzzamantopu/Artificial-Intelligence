def find_largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
number1 = 10
number2 = 20
largest = find_largest(number1, number2)    
print(f"The largest number between {number1} and {number2} is: {largest}")