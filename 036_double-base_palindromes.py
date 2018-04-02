# coding: utf-8
# 036_double-base_palindromes.py


def is_palindrome(num):
	num = str(num)
	return num == num[::-1]


total = 0

for i in range(1, 1000001):
	if is_palindrome(i) and is_palindrome(bin(i)[2:]):
		total += i

print(total)
				



