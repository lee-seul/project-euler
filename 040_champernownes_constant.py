# coding: utf-8
# 040_champernownes_constant.py


result = '0.'
num = 1
while(len(result)<=10**7+2):
	result += str(num)
	num+=1


n_list = [10**i for i in range(7)]

total = 1
for n in n_list:
	total *= int(result[n+1])

print(total)


