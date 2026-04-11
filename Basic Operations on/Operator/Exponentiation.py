""" Positive exponent
In this code snippet, we show how to calculate exponentiation using positive exponents. For example, 2 raised to the power of 3 is calculated as 2 × 2 × 2, resulting in 8. Similarly, -10 raised to the power of 4 is calculated as -10 × -10 × -10 × -10, resulting in 10000. """

base = 2
exponent = 3
print(base**exponent)  # Output: 8

base = -10
exponent = 4
print(base**exponent)  # Output: 10000



""" Negative exponent
This code computes the result of raising a base to a negative exponent. For example, 5 raised to the power of -2 equals 0.04. Similarly, 25 raised to the power of -5 results in a very small value represented in scientific notation (1.024e-07). """

base = 5
exponent = -2
print(base**exponent) # 0.04

base = 25
exponent = -5
print(base**exponent) # 1.024e-07

""" 
Floating point exponent
The code examples show that Python correctly calculates the result of raising a positive base like 2 to a fractional exponent like 1.5. However, using a negative base with a fractional exponent results in a complex number. 
"""

base = 2
exponent = 1.5
print(base**exponent) # 2.8284271247461903

base = -0.25
exponent = 1.25
print(base**exponent) # (-0.12500000000000003-0.125j)

""" 
Basic exponentiation
For basic calculations, simply provide the base and exponent to the function, which works similarly to the ** operator. """

r = pow(2, 3)
print(r) # 8

r = pow(4, -10)
print(r) # 2.56e-06


""" Floating-point exponentiation
In the code below, we're using floating-point numbers for both bases and exponents, some of which are negative. This approach works similarly to the ** operator. """

r = pow(3.5, 2)
print(r)  # 12.25

r = pow(3.5, -2)
print(r)  # 0.08163265306122448

r = pow(3.5, 3.2)
print(r)  # 55.08301986166747

r = pow(-3.5, -3.3)
print(r)  # (-0.009414432347757688+0.012957854474952653j)

r = pow(-3.5, 3.3)
print(r)  # (-36.698070584660925-50.510560868902246j)


#more examples of exponentiation
#https://www.datacamp.com/tutorial/exponents-in-python