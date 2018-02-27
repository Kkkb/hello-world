# -- coding:utf-8 --

#定义名为cheese_and_carckers的函数，接收两个参数cheese_count和boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"

# 直接赋予数字
cheese_and_crackers(20,30)

# 我们可以在脚本中使用变量
print "OR, we can use variables from our script:"

# 变量amount_of_cheese获得值10
amount_of_cheese = 10

# 将50赋值给变量amount_of_crackers
amount_of_crackers = 50

# 使用函数cheese_and_crackers，接收两个变量作为参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 参数可做数学运算
print "We can even do math inside too:"

# 调用函数cheese_and_crackers，传递两个运算参数
cheese_and_crackers(10 + 20, 5 + 6)

# 打印一行字符串，说明以下代码
print "And we can combine the two, variables and math:"

# 运行函数cheese_and_crackers,传递两个变量和运算结合的参数 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "---------------------------------------------------"
# 自己编至少一个函数出来，然后用10种方法运行这个函数
def add(first, second, third):
	sum = first + second + third
	print "%r + %r + %r = %r" % (first, second, third, sum)

add(1, 2, 3)

add(1 + 0, 2 + 1, 3 + 3)

a = 1
b = 2
c = 3
add(a, b, c)

add(a + 1, b + 1, c + 1)

a1 = raw_input("a1 = ")
a2 = raw_input("a2 = ")
a3 = raw_input("a3 = ")
add(a1, a2, a3)

# 还有什么其他不同的方法？