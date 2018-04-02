# coding: utf-8
# 038_pandigital_multiples.py


def plus_string(string_list):
	result = ''
	for i in string_list:
		result += str(i)
	return result

def check_pandigital(num):
	num = list(str(num))
	num.sort()
	standard_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	return num == standard_list


result_list = []

for number in range(1, 10000):
	n = 0
	string_list = []
	while(True):
		n += 1
		string_list.append(number*n)
		result = plus_string(string_list)
		if len(result)==9 and check_pandigital(result):
			result_list.append(result)
			break
		elif len(result)>10:
			break
		

print(max(result_list))


