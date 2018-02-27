# -- coding:utf-8 --
# 导入模组sys的argv功能
from sys import argv

# 对argv解包，将脚本的参数传递给input_file
script, input_file = argv

# 定义函数print_all，接收参数f
def print_all(f):
	# 读取f，并打印
	print f.read()

# 定义函数rewind，给予参数f
def rewind(f):
	# 调用seek方法
	f.seek(0)

# 定义函数print_a_line，它接收两个参数，行号，文件
def print_a_line(line_count, f):
	#打印行号，对f调用readline方法
	print line_count, f.readline()

# 将输入文件传递给open方法，并将其返回值传递给current_file
current_file = open(input_file)

#打印整个文件
print "First let's print the whole file:\n"

# 将文件对象传递给我们定义好的方法
print_all(current_file)

# 
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)