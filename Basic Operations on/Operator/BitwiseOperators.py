"""Bitwise operators demonstration

This module shows Python's bitwise operators with clear examples and output:

- `&`  (AND): bitwise AND
- `|`  (OR): bitwise OR
- `^`  (XOR): bitwise exclusive OR
- `~`  (NOT): bitwise NOT (two's complement; results are negative for integers)
- `<<` (left shift): shift bits left (multiply by powers of two)
- `>>` (right shift): shift bits right (floor divide by powers of two for positives)

Examples include integer values, binary displays using ``bin()``, and short notes.
"""

def show_bits(value, bits=8):
	"""Return a binary string for `value` with `bits` bits (two's complement for negatives)."""
	if value >= 0:
		return format(value, '#0{}b'.format(bits + 2))
	# for negative numbers, show two's complement with given width
	mask = (1 << bits) - 1
	return '0b' + format(value & mask, '0{}b'.format(bits))


def main():
	a = 0b1010  # 10
	b = 0b1100  # 12

	print('a =', a, show_bits(a, bits=8))
	print('b =', b, show_bits(b, bits=8))
	print()

	print('a & b ->', a & b, show_bits(a & b, bits=8))   # AND
	print('a | b ->', a | b, show_bits(a | b, bits=8))   # OR
	print('a ^ b ->', a ^ b, show_bits(a ^ b, bits=8))   # XOR
	print('~a ->', ~a, show_bits(~a, bits=8))            # NOT (two's complement)
	print()

	print('a << 1 ->', a << 1, show_bits(a << 1, bits=8))  # left shift (multiply by 2)
	print('b >> 2 ->', b >> 2, show_bits(b >> 2, bits=8))  # right shift (floor divide by 4)
	print()

	# Notes / examples with negative values
	n = -5
	print('n =', n, show_bits(n, bits=8))
	print('~n ->', ~n, show_bits(~n, bits=8))


if __name__ == '__main__':
	main()

