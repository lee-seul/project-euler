# coding: utf-8
# 029_distinct_powers.py


result_list = []

for i in range(2, 101):
	for j in range(2, 101):
		result_list.append(i**j)


print(len(set(result)))


