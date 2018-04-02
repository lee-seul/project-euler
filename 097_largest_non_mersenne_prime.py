# coding: utf-8
# 097_largest_non_mersenne_prime.py

def non_mersenne_last_10_digit():
    result = 28433
    for i in range(7830457):
        result *= 2
        result = int(str(result)[-10:])
    return print(result + 1)


non_mersenne_last_10_digit()



