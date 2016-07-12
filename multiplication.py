#!/usr/bin/python
# coding=UTF-8
print'请输入乘法表阶数。\nPlease enter the order of the multiplication table.'
order = input()
a = 1
b = 1
print 'Standard form? 1 for yes, 0 for no'
decision = input()
while decision != 1 and decision != 0:
	print 'Input not valid. Please enter 1 or 0'
	decision = input()
while a <= order:
	L = []
	while b <= order:
		L = L + [a*b]
		if decision:
			if a*b < 10:
				L = L + ['xx']
			else:
				L = L + ['x']
		b = b + 1
	print L
	b = 1
	a = a + 1