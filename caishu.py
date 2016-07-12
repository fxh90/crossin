#!/usr/bin/python
# coding=UTF-8
print '\n请输入一个1～100的整数。\nPlease enter an interger in the interval from 1 to 100.\n'
counter = 0
import random
a = random.randint(1,100)
b = input()
counter = counter + 1
while b != a:
	if b > 100 or b < 1:
		print '\n你输入的数不在范围内。\nYour guess is out of range.\n'
	elif b < a:
		print '\n太小了，请再猜一次。\nYour guess is too small. Please have another guess.\n'
	elif b > a:
		print '\n太大了，请再猜一次。\nYour guess is too large. Please have another guess.\n'
	b = input()
	counter = counter + 1
print '\n恭喜您猜对了！答案是''',a,'！您在',counter,'次内猜中了！\nCongratulations! Your guess is correct! The auswer is',a,'! You got the answer in',counter,'times!\n'