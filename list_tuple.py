Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List
a=[4,6.7,"python",5+9j,True,False]
a
[4, 6.7, 'python', (5+9j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>
a=["python","c","java"]
a.append("html")
a
['python', 'c', 'java', 'html']
a.append("css","js")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("css","js")
TypeError: list.append() takes exactly one argument (2 given)
a.extend(["css","js"])
a
['python', 'c', 'java', 'html', 'css', 'js']
a.append(["css","js"])
a
['python', 'c', 'java', 'html', 'css', 'js', ['css', 'js']]
a=["apple","banana"]
a.extend("grapes","pineapple")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.extend("grapes","pineapple")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["grapes","pineapple"])
a
['apple', 'banana', 'grapes', 'pineapple']
a.insert(1,"custard apple")
a
['apple', 'custard apple', 'banana', 'grapes', 'pineapple']
## insert() and extend()

#clear()
a.clear()
a
[]
#copy()
b=["c","java","c++"]
b.copy()
['c', 'java', 'c++']
#index
b.index("java")
1
a.append("data")
a
['data']
#sort
a=["white","balck","pink","brown"]
a.sort()
a
['balck', 'brown', 'pink', 'white']
b=[1,7,3,5,2,6,8]
b.sort()
b
[1, 2, 3, 5, 6, 7, 8]
b=[44,77,22,134]
b.sort()
b
[22, 44, 77, 134]
#reverse
a=[2,4,5,6,7,32,45]
a.reverse()
a
[45, 32, 7, 6, 5, 4, 2]
b=[happy,how,ha]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b=[happy,how,ha]
NameError: name 'happy' is not defined
b=["happy","how","ha"]
b.reverse()
b
['ha', 'how', 'happy']
a.sort(::-1)
SyntaxError: invalid syntax
a.sort[::-1]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.sort[::-1]
TypeError: 'builtin_function_or_method' object is not subscriptable
a[::-1]
[2, 4, 5, 6, 7, 32, 45]
a.sort(reverse=True)
a
[45, 32, 7, 6, 5, 4, 2]
#pop
a=[3,5,4,2,6,7,5]
a.pop()
5
a
[3, 5, 4, 2, 6, 7]
a.pop(4)
6
a
[3, 5, 4, 2, 7]
b=[5,3,5,2,6,8]
b.remove(2)
b
[5, 3, 5, 6, 8]
b=[7,7,3,2,4]
b.remove(7)
b
[7, 3, 2, 4]
#length
a=[3,6,4,6,8,1]
len(a)
6
a="hello"
len(a)
5
b=["hello"]
len(b)
1
a.count(6)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.count(6)
TypeError: count() argument 1 must be str, not int
b.count('l')
0
b="hello"
b.count('l')
2

#tuple
a=(2,5,4,3,7,8)
type(a)
<class 'tuple'>
a.index(5)
1
b=(1,"python")
b=(3,5,3,6,7,8,20)
b.count(3)
2
len(a)
6

#task
a=[9,1,5,2,8,4,6,3,7,0]
a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
a
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a.replace(0,7)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.replace(0,7)
AttributeError: 'list' object has no attribute 'replace'
a.insert(1,7)
a
[9, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a.insert(0,7)
a
[7, 9, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a.insert(1,6)
a
[7, 6, 9, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a.insert(2,4)
a
[7, 6, 4, 9, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a.insert(3,3)

>>> a
[7, 6, 4, 3, 9, 7, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a.insert(4,0)
>>> a.insert(5,9)
>>> a.clear()
>>> a.extend(7,6,4,3,0,9,8,5,2,1)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.extend(7,6,4,3,0,9,8,5,2,1)
TypeError: list.extend() takes exactly one argument (10 given)
>>> a.extend([7,6,4,3,0,9,8,5,2,1])
>>> a
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.reverse()
>>> a
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
>>> a.extend[7,6]
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.extend[7,6]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a[:5]
[0, 7, 3, 6, 4]
>>> a[5:]
[8, 2, 5, 1, 9]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[:5:]
[9, 1, 5, 2, 8]
>>> a[5:]
[4, 6, 3, 7, 0]
>>> a1=a[:5]
>>> a2=a[5:]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a1.sort()
a1
[1, 2, 5, 8, 9]
a=[9,1,5,2,8,4,6,3,7,0]
a1=a[:5]
a2=a[5:]
a.sort()
a1.sort()
a2.sort()
a1.reverse()
a2.reverse()
c=a2+a1
c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]


