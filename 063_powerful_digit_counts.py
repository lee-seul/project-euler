# coding: utf-8
# 063_powerful_digit_counts.py


def digit_counts(num, pow_num):
	return len(str(num**pow_num)) == pow_num


count = 0
for i in range(1, 10):
	for j in range(1, 100):
		if digit_counts(i,j):
			count += 1

print(count)



