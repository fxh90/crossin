# coding=UTF-8
from random import randint
total_amount = input('请输入红包总金额\n')
num = input('请输入人数\n')
amount_left = float(total_amount)
for i in range(num-1):
	a = randint(1,int(100*amount_left-(num-i-1)))
	a = float(a)/100
	print '%.2f'%a
	amount_left = amount_left - a
print '%.2f'%amount_left