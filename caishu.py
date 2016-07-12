#!/usr/bin/python
# coding=UTF-8
try:
	f = open('caishu.txt')
	data = f.readlines()
	f.close()
except:
	f = open('caishu.txt','w')
	f.close()
	data = []
dic = {}
for l in data:
	s = l.split()
	dic[s[0]] = s
print 'What is your name?'
name = raw_input()
score = dic.get(name)
if score == None:
	score = [name,'0','0','0']
print '\n请输入一个1～100的整数。\nPlease enter an interger in the interval from 1 to 100.\n'
counter = 0
import random
a = random.randint(1,100)
while 1 == 1:
	try:
		b = input()
		break
	except:
		continue
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
print '\n恭喜您猜对了！答案是%d！您在%d次内猜中了！\nCongratulations! Your guess is correct! The answer is %d! You got the answer in %d times!' %(a,counter,a,counter)
total_time = int(score[1]) + 1
if int(score[2]) == 0 or int(score[2]) > counter:
	min_time = counter
else:
	min_time = int(score[2])
total_count = int(score[3]) + counter
if total_time == 0:
	avg = 0
else:
	avg = float(total_count) / total_time
print '截至目前，您进行了%d次游戏，平均%.2f次猜中，最少%d次猜中！'%(total_time,avg,min_time)
output = []
dic[name] = [name,str(total_time),str(min_time),str(total_count)]
for g in dic:
	string = ' '.join(dic[g]) + '\n'
	output.append(string)
f = open('caishu.txt','w')
f.writelines(output)
f.close()