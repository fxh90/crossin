#!/usr/bin/python
# coding=UTF-8
print'请输入乘法表阶数。\nPlease enter the order of the multiplication table.'
order = input()
a = 1
b = 1
for a in range(1,order+1):
	while b in range(1,order+1):
		print a*b,
		b += 1
	print
	b = 1
	a += 1