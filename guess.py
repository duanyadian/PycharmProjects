#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:段亚典

"""
_username="段亚典"
_password="123456"
username = input("username:")
password = input("password:")
if _username == username and _password == password:
	print("欢迎{name}，登录成功!".format(name = username))
else:
	print("用户名或密码错误!")
"""
"""
age_of_dyd = 18
guess_of_dyd =int(input("age_of_dyd:"))
if guess_of_dyd == age_of_dyd:
	print("Yes,You got it!恭喜，你猜中了！")
elif guess_of_dyd >age_of_dyd:
	print("Think bigger!猜大了！")
else:
	print("Think Smaller!猜小了！")
"""


"""
age_of_dyd = 18
count =1
while count <3:
	guess_of_dyd =int(input("age_of_dyd:"))
	if guess_of_dyd == age_of_dyd:
		print("Yes,You got it!恭喜，你猜中了！")
		break
	elif guess_of_dyd >age_of_dyd:
		print("Think bigger!猜大了！")
	else:
		print("Think Smaller!猜小了！")
	count +=1
else:
	print("错误次数过多，游戏结束！")
"""


age_of_dyd = 18
count =1
while count <3:
	guess_of_dyd =int(input("age_of_dyd:"))
	if guess_of_dyd == age_of_dyd:
		print("Yes,You got it!恭喜，你猜中了！")
		break
	elif guess_of_dyd >age_of_dyd:
		print("Think bigger!猜大了！")
	else:
		print("Think Smaller!猜小了！")
	count +=1
	if count == 3:
		continue_confirm = input("游戏结束，是否继续？")
		if continue_confirm != "n":
			count = 0
else:
	print("错误次数过多，游戏结束！")


"""
age_of_dyd = 18
for i in range(3):
	guess_of_dyd =int(input("age_of_dyd:"))
	if guess_of_dyd == age_of_dyd:
		print("Yes,You got it!恭喜，你猜中了！")
		break
	elif guess_of_dyd >age_of_dyd:
		print("Think bigger!猜大了！")
	else:
		print("Think Smaller!猜小了！")
else:
	print("错误次数过多，游戏结束！")
"""