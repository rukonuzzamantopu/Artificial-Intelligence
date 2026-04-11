"""Minimal `if`-only examples

This file shows simple `if` statements without `else`/`elif`. Each example performs
an action only when the condition is True.
"""


def check_positive(x):
    if x > 0:
        print(x, "is positive")


def check_even(x):
    if x % 2 == 0:
        print(x, "is even")


def check_divisible_by_three(x):
    if x % 3 == 0:
        print(x, "is divisible by 3")


def check_in_range(x):
    # action only when x is inside the range 1..10
    if 1 <= x <= 10:
        print(x, "is between 1 and 10")


def greet_morning(hour):
    # greet only if it's morning (6-11)
    if 6 <= hour <= 11:
        print("Good morning")


def main():
    print('--- simple_if examples ---')
    check_positive(5)
    check_positive(-2)

    check_even(4)
    check_even(7)

    check_divisible_by_three(9)
    check_divisible_by_three(10)

    check_in_range(5)
    check_in_range(20)

    greet_morning(8)
    greet_morning(14)


if __name__ == '__main__':
    main()
