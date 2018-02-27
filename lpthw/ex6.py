# -- coding:utf-8 -- 
#Python通过双引号或单引号识别字符串

# 将变量x赋值给一个带有格式化字符串的字符串"There are %d types of people."
x = "There are %d types of people." % 10

# 将字符串"binary"赋值给变量binary
binary = "binary"

#变量do_not获得"don't"这个字符串
do_not = "don't"

# 1.变量y获得字符串"Those who know %s and those who %s."，带有两个格式化字符串，值为binary和do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# 打印变量x
print x

# 2.输出变量y
print y

# 3.打印一个带有格式化字符的字符串，格式化字符的值为变量x
print "I said: %r." % x

# 4.打印一个带有格式化字符串的字符串，格式化字符的值为变量y
print "I also said: '%s'." % y

# 变量hilarious获得布尔值False
hilarious = False

# 变量joke_evaluation获得字符串"Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印joke_evaluation,其格式化字符串的值为hilarious
print joke_evaluation % hilarious

# 变量w获得字符串"This is the left side of..."
w = "This is the left side of..."

# 变量e获得字符串"a string with a right side."
e = "a string with a right side."

# 打印两字符串的和
print w + e