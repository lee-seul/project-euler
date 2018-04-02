# coding: utf-8
# 031_coin_sum.py


coins = [1, 2, 5, 10, 20, 50, 100, 200]
result = {i:0 for i in range(1, 201)}

for coin in coins:
	result[coin] += 1
	for j in range(coin+1, 201):
		result[j] += result[j-coin]

print(result[200])

	
