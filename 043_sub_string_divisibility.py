# coding: utf-8
# 043_sub_string_divisibility.py

from itertools import permutations

number = '1234567890'
pm_list = list(permutations(number))


result = 0

prime_list = [2, 3, 5, 7, 11, 13, 17]


for index_pm in range(len(pm_list)):
	string = ''
	n = 0
	if pm_list[index_pm][0] != '0':
		for num in range(1, len(pm_list[index_pm])-2):
			string += pm_list[index_pm][num] + pm_list[index_pm][num+1] +\
					pm_list[index_pm][num+2]
			if int(string) % prime_list[num-1] != 0:
				break
			else:
				string = ''
				n+=1
		if n == 7:
			string = ''
			for x in pm_list[index_pm]:
				string += x
			result += int(string)

print(result)


