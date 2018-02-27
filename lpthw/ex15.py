# -- coding:utf-8 --

# 导入sys模组的argv功能
from sys import argv

# 对argv进行解包，将它的值赋予filename
script, filename = argv

# open命令接受filename，返回一个文件对象，并赋予给变量txt，即打开文件的过程
txt = open(filename)

# 打印文件名称
print "Here's your file %r:" % filename

# 对txt文件对象执行read命令，并将其打印
print txt.read()

# 另外一种打开文件的方法，采用raw_input接受文件名
print "Type the filename again:"

# 从用户处获取文件名
file_again = raw_input("> ")

# 打开文件
txt_again = open(file_again)

# 读取文件
print txt_again.read()

# 关闭文件
txt.close()
txt_again.close()