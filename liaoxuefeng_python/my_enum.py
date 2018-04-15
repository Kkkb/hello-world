from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', \
			 'Apr', 'May', 'Jun', 'Jul', \
			 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

'''
python my_enum.py
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
'''