"""
File: largest_digit.py
Name: Willie Li
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, eliminate the last number of the integer
	:return: the max number of the input integer
	"""
	if n < 0:
		n = -n
		return find_largest_digit(n)
	elif 0 < n < 10:
		return n
	else:
		# get the number
		number_1 = n - (n // 10) * 10
		rest_num = (n - number_1) // 10
		max_number = find_largest_digit(rest_num)
		if number_1 > max_number:
			return number_1
		return max_number


if __name__ == '__main__':
	main()
