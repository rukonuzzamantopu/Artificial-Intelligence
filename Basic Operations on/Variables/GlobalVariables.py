""" Variables that are created outside of a function (as in all of the examples above) are known as global vari
ables.Global variables can be used by everyone, both inside of functions and outside. """

x="Topu"
def myfun():
    print("my name is " +x)

myfun()


""" If you create a variable with the same name inside a function, this variable will be local, and can only be used
inside the function. The global variable with the same name will remain as it was, global and with the original
value. """

x="Topu"
def myfun():
    x="Ashab"
    print("my name is " +x)
myfun()
print(x)


""" Normally, when you create a variable inside a function, that variable is local, and can only be used inside that
function.
To create a global variable inside a function, you can use the global keyword. """

def myfun():
    global x
    x="Alma"
myfun()
print("she is a good girl: " + x)

""" Also, use the global keyword if you want to change a global variable inside a function. """

x="Topu"
def myfun():
    global x
    x="Ashab"
myfun()
print("my name is " + x)