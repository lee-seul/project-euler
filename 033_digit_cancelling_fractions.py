# coding: utf-8
# 033_digit_cancelling_fractions.py


def digit_cancelling(num1, num2):
	cancel_num = set(str(num1))&set(str(num2))
	if cancel_num:
		cancel_num = list(cancel_num)[0]
		a = list(str(num1))
		a.remove(cancel_num)
		b = list(str(num2))
		b.remove(cancel_num)
		return num1/num2 == int(a[0])/int(b[0])
	return False

l = [i for i in range(10, 100) if i % 10 != 0]

x = 1
y = 1
for i in l:
	for j in l:
		if i/j < 1 and digit_cancelling(i, j):
			x *= i
			y *= j

print(y/x)
			



