"""If-statement examples

This file demonstrates common `if`-related patterns in Python with concise, runnable
examples:

- simple `if` / `else`
- `if` / `elif` / `else`
- nested `if`
- chained comparisons
- membership checks with `in`
- conditional (ternary) expression

Run the file to see expected outputs.
"""


def simple_if(x):
	if x > 0:
		return "positive"
	else:
		return "non-positive"


def if_elif_else(score):
	if score >= 90:
		return "A"
	elif score >= 75:
		return "B"
	elif score >= 60:
		return "C"
	else:
		return "F"


def nested_if(age, has_permission):
	if age >= 18:
		if has_permission:
			return "Allowed"
		return "Needs permission"
	return "Too young"


def chained_and_membership(n, seq):
	# chained comparisons and membership
	if 0 < n < 10 and n in seq:
		return "n is a small positive number and present"
	return "no match"


def ternary_example(a, b):
	# conditional expression (ternary)
	return a if a >= b else b


def main():
	print("simple_if(5) ->", simple_if(5))
	print("simple_if(0) ->", simple_if(0))

	print("if_elif_else(92) ->", if_elif_else(92))
	print("if_elif_else(80) ->", if_elif_else(80))
	print("if_elif_else(50) ->", if_elif_else(50))

	print("nested_if(20, True) ->", nested_if(20, True))
	print("nested_if(20, False) ->", nested_if(20, False))
	print("nested_if(15, True) ->", nested_if(15, True))

	seq = [2, 4, 6, 8]
	print("chained_and_membership(4, seq) ->", chained_and_membership(4, seq))
	print("chained_and_membership(12, seq) ->", chained_and_membership(12, seq))

	print("ternary_example(3,5) ->", ternary_example(3, 5))
	print("ternary_example(7,2) ->", ternary_example(7, 2))


if __name__ == '__main__':
	main()

