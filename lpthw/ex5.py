# -*- coding:utf-8 -*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r inches tall." % height # 格式化字符%r 不管什么都打印出来 
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "****************************************"
# 1英寸 = 2.54厘米
inches = 1
#inches = height
centimeter = inches * 2.54
print "%d inches = %r centimeters" % (inches, centimeter)