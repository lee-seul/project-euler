# coding: utf-8
# 030_digit_fifth_powers.py


def digit_fifth_powers_sum(num):
	result = sum([int(i)**5 for i in list(str(num))])
	return num == result

total = 0
for i in range(2, 354295):
	if digit_fifth_powers_sum(i):
		total += i

print(total)



