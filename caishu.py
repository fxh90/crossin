#!/usr/bin/python
# coding=UTF-8
print '''
请输入一个1～100的整数。
Please enter an interger in the interval from 1 to 100.
'''
import random
a = random.randint(1,100)
b = input()
for c in range(1,100):
	if b > 100 or b < 1:
		print '''
你输入的数不在范围内。
Your guess is out of range.
'''
		b = input()
	elif b < a:
		print '''
太小了，请再猜一次。
Your guess is too small. Please have another guess.
'''
		b = input()
	elif b > a:
		print '''
太大了，请再猜一次。
Your guess is too large. Please have another guess.
'''
		b = input()
	elif b == a:
		print '''
恭喜您猜对了！答案是'''
		print a
		print '''
Congratulations! Your guess is correct! The auswer is'''
		print a
		break
	else:
		print '请重新输入 Please retry'
		b = input()