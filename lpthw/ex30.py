# -*- coding:UTF-8 -*-
# 将右边的值赋予给左边的变量
people = 100
cars = 80
buses = 60

# 如果布尔表达式为Ture，则执行输出"We should take the cars."并跳过剩下的判断，为False则调至下一句判断
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars"
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Mybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if cars > people and buses < cars:
	print "True"
else:
	print "False"