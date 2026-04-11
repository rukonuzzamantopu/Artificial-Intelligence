# Program to find factorial of a number using while loop

num = int(input("Enter a number: "))

factorial = 1
i = 1

# Check negative number
if num < 0:
    print("Factorial does not exist for negative numbers")

else:
    while i <= num:
        factorial *= i
        i += 1

    print("Factorial of", num, "is", factorial)

    #output:
    #Enter a number: 5
    #Factorial of 5 is 120
    