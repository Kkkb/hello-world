## 编程基础测试题

* 来源[知乎](https://zhuanlan.zhihu.com/p/21102354)


### [题 1](#题1)
```python
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10

def valid_password(pwd):
    pass
```


### [题 2](#题2)
```python
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
    pass
```


### [题 3](#题3)
```python
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

def letter_count(str):
    pass
```


### [题 4](#题4)
```python
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

def cap_string(str):
    pass

```

### [题 5](#题5)
```python
# 写一个 Queue 类，它有两个方法，用法如下

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
```


### 题1
```python
def valid_password(pwd):
	if not (2 <= len(pwd) <= 10):
		return False

	if not pwd[0].isalpha():
		return False

	for p in pwd[1:-1]:
		if not (p.isalnum() or p == "_"):
			return False

	if not pwd[-1].isalnum():
		return False

	return True
```

### 题2
```python
def prime_numbers():
	pn = []
	for n in range(2, 101):
		t = 0
		for s in range(1, n + 1):
			if n % s == 0:
				t += 1
		if t == 2:
			pn.append(n)
	return pn
```

### 题3
```python
def letter_count(str):
	d = {}
	l = list(str)
	for s in str:
		d[s] = l.count(s)
	
	r = []
	for k in d:
		r.append((k, d[k]))
	return r
```

### 题4
```python
def cap_string(str):
	cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', \
		   'H', 'I', 'J', 'K', 'L', 'M', 'N', \
		   'O', 'P', 'Q', 'R', 'S', 'T', 'U', \
		   'V', 'W', 'X', 'Y', 'Z']
	low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
		   'h', 'i', 'j', 'k', 'l', 'm', 'n', \
		   'o', 'p', 'q', 'r', 's', 't', 'u', \
		   'v', 'w', 'x', 'y', 'z']

	if str[0] in cap:
		s = str[0]
	else:
		s = cap[low.index(str[0])]
	
	for i in str[1:]:
		if i in low:
			s += i
		else:
			s += low[cap.index(i)]
	return s
```

### 题5
```python
class Queue(object):
	def __init__(self):
		self.q = []

	def enqueue(self, number):
		self.q.append(number)

	def dequeue(self):
		return self.q.pop(0)

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)

	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())
```