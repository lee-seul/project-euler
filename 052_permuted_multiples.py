# coding: utf-8
# 052_permuted_multiples.py



def comparison_number(num1, num2):
	num1 = list(str(num1))
	num2 = list(str(num2))
	num1.sort()
	num2.sort()
	return num1 == num2


n = 1


while(True):
	true = 0
	for i in range(2, 7):
		if comparison_number(n, n*i):
			true += 1
		else:
			break
	if true == 5:
		print(n)
		break
	else:
		n += 1
		



