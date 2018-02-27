# -*- coding: utf-8 -*-
dict = {'Baidu': 'www.baidu.com', 'Google': 'www.google.com', 'Kkkb': 'kkkb.github.io'}
print dict
print dict.items()

# 将for-loop执行到dict上面
for i in dict:
	print i #打印的是键

# 试着在for-loop中使用dict的items()函数
for i in dict.items():
	print i

for key,values in dict.items():
	print key,values