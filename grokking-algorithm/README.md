`大O表示法`代表算法的速度有多快(算法的运行时间如何随列表的增加而增加)

二分查找的运行时间为O(logn),对数时间

简单查找 O(n),线性时间

链表擅长插入 删除元素

数组擅长读取元素

某些情况下，递归易于理解，但性能没有循环好

调用栈(call stack)

栈是一种简单的数据结构，函数的调用采用调用栈这种数据结构

递归函数使用调用栈

(divide and conquer, D&C) 分而治之，一种著名的递归式问题解决方法

递归指的是调用自己的函数，每个递归函数都有两个条件，基线条件和递归条件

所有函数调用都进入调用栈，如果调用栈很长，将占用大量内存

Haskell等函数式编程语言没有循环，只能使用递归来编写函数

merge sort 合并排序

快速排序的平均运行时间为O(nlogn)

散列表(hash table),也称为散列映射、映射、字典和关联数组，它使用散列函数确定元素的存储位置。DNS由散列表实现，网页缓存的数据存储在散列表中

广度优先搜索(breadth-first serch, BFS)是一种图算法

图由节点(node)和边(edge)组成

队列(queue)只支持两种操作：入队和出队。

队列是一种*先进先出*(First In First Out, FIFO)的数据结构，栈是一种*后进先出*(Last In First Out, LIFO)的数据结构

树是一种特殊的图，没有往后指的边

狄克斯特拉算法(Dijkstr's algorithm)

