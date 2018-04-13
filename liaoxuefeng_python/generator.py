# -*- coding: utf-8-*-
'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，
不断输出下一行的list：
'''

def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]