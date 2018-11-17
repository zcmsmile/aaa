#!/usr/bin/python3
#-*- coding:utf-8 -*-
def fun(n):
	if n==1:
		return 1
	else:
		return n*fun(n-1)
while True:
	num=int(input('请输入数字：'))
	print(fun(num))
