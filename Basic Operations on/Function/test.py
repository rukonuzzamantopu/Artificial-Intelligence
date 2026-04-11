""" Functions enable you to break down the overall functionality of a script into smaller, logical subsections. These subsections can then be called upon to perform their individual tasks when needed.

Using functions to perform repetitive tasks is an excellent way to create code reuse. This is an important part of modern object-oriented programming principles.

In Python, a function is defined using the def keyword. """



def my_fun():
    """ This is a simple function that prints a message. """
    print("Hello, World!")
my_fun()  # Output: Hello, World!

#------------------
#passing arguments to a function

def my_func(name):
    print("name is " + name)
my_func("Topu")
my_func("Kawser")
my_func("Hridoy")

# Output:
# name is Topu
# name is Kawser
# name is Hridoy

#------------------

#passing multiple arguments to a function

def my_funcs(fname ,lname):
    print("full name is " + fname + " " + lname)

    my_funcs("Rukonuzzamn","Topu")
    my_funcs("amdadul","Kawser")
    my_funcs("Hridoy","Ahmed")

# Output:
# full name is Rukonuzzamn Topu
# full name is amdadul Kawser
# full name is Hridoy Ahmed

#------------------

#arbitary arguments,*args

def my_arbitary(*args):
    print("the first name is " + args[0])
    print("the second name is " + args[1])
    print("the third name is " + args[2])

my_arbitary("Rukonuzzamn","Topu","Kawser")

# Output:
# the first name is Rukonuzzamn

# the second name is Topu
# the third name is Kawser

#------------------

#send argument with the key =value syntax

def my_myfunction(name3,name2,name1):
    print("Name is " + name1)

my_myfunction(name1 = "Alma", name2 ="Topu",name3="Kawser")

# Output:
# Name is Alma

def my_myfunction(**name):
    print("His last name is " + name["lname"])

my_myfunction(fname = "Nishat Tasnim" , lname ="Alma")

""" Summary 🧠
** means collect keyword arguments
It stores them as a dictionary
It allows flexible number of named inputs
Access values using keys like name["lname"] """


# Output:
# His last name is Alma


#------------------

# ================================
# 1. PASSING A LIST INTO A FUNCTION
# ================================

# This function takes a LIST as input (called 'food')
# and prints each item one by one.
def my_function(food):
    # 'food' is a list (example: ["orange", "apple", "cherry"])

    for i in food:
        # Loop through each element in the list
        # 'i' will take one value at a time
        print(i)
        # Each item is printed on a new line


# Creating a list of fruits
fruits = ["orange", "apple", "cherry"]

# Sending the list to the function
my_function(fruits)


# ================================
# 2. RETURN VALUE FUNCTION
# ================================

# This function takes a number 'a'
# and returns 5 times that number
def my_function(a):
    # 'return' sends the result back to where function was called
    # It does NOT print directly, it gives a value
    return 5 * a


# Calling function with different values
print(my_function(3))  # 5 * 3 = 15
print(my_function(5))  # 5 * 5 = 25
print(my_function(9))  # 5 * 9 = 45


# ================================
# 3. RECURSION EXAMPLE
# ================================

# Recursion means a function calling itself
# This function calculates sum from k down to 0

def my_recursion(k):

    # BASE CASE (VERY IMPORTANT)
    # When k becomes 0, function stops calling itself
    if k > 0:

        # Recursive call: function calls itself with smaller value (k-1)
        # This builds a chain like:
        # 6 + my_recursion(5)
        # 5 + my_recursion(4)
        # and so on...

        result = k + my_recursion(k - 1)

        # After returning from deeper calls,
        # it prints the current accumulated result
        print(result)

        # return the result back to previous call
        return result

    else:
        # Base case: when k == 0, stop recursion
        # This prevents infinite loop
        return 0


# Starting point of recursion
print("\nRecursion Example Results")

# This starts the recursion chain
my_recursion(6)

