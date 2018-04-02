# coding: utf-8
# 057_square_root_convergents.py


numerator_list = [1, 3]
denominator_list = [1, 2]

for i in range(1, 1001):
	numerator_list.append(numerator_list[i]*2+numerator_list[i-1])
	denominator_list.append(denominator_list[i]*2+denominator_list[i-1])

# 분자, 분모 각각 다음항은 현재 항에 2를 곱한 후 이전 항을 더하면 구할 수 있다.

count = 0
for i in range(1, 1001):
	if len(str(numerator_list[i])) > len(str(denominator_list[i])):
		count += 1


print(count)




