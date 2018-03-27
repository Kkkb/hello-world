Python同时支持面向过程编程与面向对象编程

Python是强(Strongly)面向对象的，因为所有的一切都是对象，包括数字、字符串与函数

可以在while循环中使用else从句

range()每次只会生成一个数字

可变参数

当我们声明一个\*param星号参数时，从此处开始直到结束的所有位置参数都会被汇集成一个“param” 的元组(Tuple)

当我们声明一个\*\*param星号参数时，从此处开始直到结束的所有关键字参数都会被汇集成一个“param”的字典(Dictionary)

return语句没有搭配任何一个值代表返回None

.pyc文件按字节码编译

当模块第一次被导入时，它所包含的代码将被执行

每一个Python模块都定义了它的__name__属性，如果它与__main__属性相同则代表这一模块是由用户独立运行的

包是指一个包含模块与一个特殊的__init__.py文件的文件夹

List, Tuple, Dictionary, Set是四种Python内置的数据结构

列表是一种可变的数据类型

列表是使用对象与类的实例

集合(Set)是简单对象的无序集合(Collection)

当创建一个对象并将其分配给某个变量时，变量只会查阅(Refer)某个对象，不代表对象本身，也就是说变量名只是指向计算机内存中存储了相应对象的那一部分。这叫做将名字绑定(Binding)给那一个对象

将装饰器想象为调用一个包装器(Wrapper)函数的快捷方式

面向对象编程通过继承(Inheritance)机制实现代码的重用(Reuse)

多态(Polymorphism)

封装(Pickling)

拆封(Unpickling)

错误处理器(Error Handler)

EOFError(End of File error)

Python 标准库(Python Standrad Library)

lambda 语句可创建一个新的函数对象，接收一个参数，后跟一个表达式作为函数体，表达式执行的值作为这个新函数的返回值。

Assert断言，当语句断言失败是，抛出AssertionError