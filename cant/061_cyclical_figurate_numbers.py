# coding: utf-8
# 061_cyclical_figurate_numbers.py

from lib.X_number import num_3, num_4, num_5, num_6, num_7, num_8



l = [[str(i)[:2], str(i)[2:] for i in range(1000, 10000)]




def is_4_digit(num):
	return len(str(num)) == 4


def is_cyclic(num1, num2):
	return str(num1)[2:] == str(num2)[:2]



num_3_list = [num_3(i) for i in range(1, 150) if is_4_digit(num_3(i))]
num_4_list = [num_4(i) for i in range(1, 150) if is_4_digit(num_4(i))]
num_5_list = [num_5(i) for i in range(1, 150) if is_4_digit(num_5(i))]
num_6_list = [num_6(i) for i in range(1, 150) if is_4_digit(num_6(i))]
num_7_list = [num_7(i) for i in range(1, 150) if is_4_digit(num_7(i))]
num_8_list = [num_8(i) for i in range(1, 150) if is_4_digit(num_8(i))]




