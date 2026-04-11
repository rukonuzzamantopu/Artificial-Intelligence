# Nested if statements
""" Nested if statements are if statements that are contained within another if statement. They allow you to check multiple conditions in a hierarchical manner. The inner if statement is only evaluated if the outer if statement's condition is true. This can be useful for checking related conditions that depend on each other. Here's an example of a nested if statement: """



x=45
if x>10:
    print("Above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")



""" In this example, we have an if statement inside another if statement. The first if statement checks if x is greater than 10, and if it is, it prints "Above ten". Then, it checks if x is also greater than 20. If it is, it prints "and also above 20". If it is not, it prints "but not above 20". In this case, since x is 45, both conditions are true, so the output will be: "Above ten" and "and also above 20".You can have as many nested if statements as you want, but it is important to keep the code readable and not to overuse nesting, as it can make the code harder to understand. """