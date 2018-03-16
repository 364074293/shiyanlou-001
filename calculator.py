#!/usr/bin/env python3
import sys
try:
	i=int(sys.argv[1])*(1-0.165)-3500
	if i>80000:
		i=i*0.45-13500
		print(format(i,'.2f'))
	elif 55000<i<=80000:
		i=i*0.35-5505
		print(format(i,'.2f'))
	elif 35000<i<=55000:
		i=i*0.3-2755
		print(format(i,'.2f'))
	elif 9000<i<=35000:
		i=i*0.25-1005
		print(format(i,'.2f'))
	elif 4500<i<=9000:
		i=i*0.20-555
		print(format(i,'.2f'))
	elif 1500<i<=4500:
		i=i*0.1-105
		print(format(i,'.2f'))
	elif 0<i<=1500:
		i=i*0.03
		print(format(i,'.2f'))
	elif -3500<i<0:
		i=0
		print(format(i,'.2f'))
	else:
		print('输入有误')
except ValueError:
	print('请输入数字：')
