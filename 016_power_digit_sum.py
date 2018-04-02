# coding: utf-8
# 016_power_digit_sum.py

def two_power_sum(num):
	two = str(2**num)
	digit_total = 0
	for x in two:
		digit_total += int(x)
	return digit_total


print(two_power_sum(1000))

