""" The else keyword catches anything which isn’t caught by the preceding conditions. """

a=200
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("b is not greater than a")

""" In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we
go to the else condition and print to screen that "a is greater than b".
You can also have an else without the elif:
 """

a=33
b=200
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

""" In this example a is not greater than b, so the first condition is not true, so we go to the else condition and print
to screen that "b is greater than a". """