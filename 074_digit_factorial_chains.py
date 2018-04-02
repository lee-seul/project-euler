# coding: utf-8
# 074_digit_factorial_chains.py

from lib.permutation_combinations import factorial


def digit_factorial(num):
	num_list =[int(i) for i in list(str(num))]
	result = 0
	for n in num_list:
		result += factorial(n)
	return result


def count_factorial_chain(num):
	chain = [num]
	while(True):
		chain_num = digit_factorial(chain[-1])
		if chain_num in chain:
			break
		else:
			chain.append(chain_num)
	return len(chain)

count = 0
for i in range(1, 1000001):
#	print(i)
	if count_factorial_chain(i) == 60:
		count += 1

print(count)

