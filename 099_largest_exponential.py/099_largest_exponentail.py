# coidng: utf-8
# 099_largest_exponentail.py

from math import log

data = open("base_exp.txt").read().split("\n")

def calcul_exponential(num, exp):
    return log(int(num)) * int(exp)

value = 0
for i in range(len(data) - 1):
    temp_list = data[i].split(",")
#    print(temp_list)
    if value < calcul_exponential(temp_list[0], temp_list[1]):
        value = calcul_exponential(temp_list[0], temp_list[1])
        result = i

print(result + 1)

