# -*- coding: utf-8 -*-
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#的两个解。

import math

def quadratic(a, b, c):
	dt = math.sqrt(abs(b*b - 4*a*c))
	x1 = (-b + dt) / (2*a)
	x2 = (-b - dt) / (2*a)
	return x1, x2