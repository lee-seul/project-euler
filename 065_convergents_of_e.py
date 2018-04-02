# coding: utf-8
# 065_convergents_of_e.py


def convergents_of_e(num):
	if num == 1:
		return 2
	elif num == 2:
		return 3
	else:
		e = [2, 1]
		for i in range(num-2):
			if i % 3 == 0:
				e.append(2*(i/3+1))
			else:
				e.append(1)
	a = 0 # 분자
	b = 0 # 분모
	tmp = 0
	for x in range(len(e)-1):
		print(x, a, b)
		x = -x - 1
		if x == -1:
			a = e[x-1] * e[x] + 1
			b = e[x]
		else:
			tmp = a
			a = b 
			b = tmp
			a = a + e[x-1]*b
	return	a


result = list(str(int(convergents_of_e(100))))
total = 0
for i in result:
	total += int(i)

print(total)



