Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={2,6.5,"python",7+9j,True,False}
print(a)
{False, True, 2, (7+9j), 'python', 6.5}
type(a)
<class 'set'>
#add()
a={2,3,4,5}
a.add(10)
a
{2, 3, 4, 5, 10}
#subset()
a={1,2,3,4,11,12,13,14}
b={11,12,13,14}
b.issubset(a)
True
#superset()
a={1,2,3,4,6,5,11,12,13,14}
b={4,3,5,6,}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={1,2,3,4,5,6,7}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6, 7}
a={4,5,6,7,8,9}
b={6,7,8,9}
a.intersection(b)
{8, 9, 6, 7}
#update
a={3,4,5,6,7,8,9}
b={5,6,7,8,9,10}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9, 10}
b
{5, 6, 7, 8, 9, 10}
a
{3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10}
b
{3, 4, 5, 6, 7, 8, 9, 10}
#difference
a={3,4,5,6,7,8}
b={5,6,7,8,9,10,11}
a.difference(b)
{3, 4}
b.difference(a)
{9, 10, 11}
#symmertric differnece
a={1,2,3,4,5,6,7}
b={2,3,5,6,7,8,7,9,10,11,12}
a.symmetric_difference(b)
{1, 4, 8, 9, 10, 11, 12}
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.intersection_update(b)
a
{13, 14, 15}
b.intersection_update(a)
b
{13, 14, 15}
#intersection_update

#difference_update
a={1,2,3,4,5,6,7,8}
b={4,5,6,7,8,9,10,11}
a.difference_update(b)
a
{1, 2, 3}
b.differnece_update(a)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.differnece_update(a)
AttributeError: 'set' object has no attribute 'differnece_update'. Did you mean: 'difference_update'?
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11}
#symmetric_difference_update
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6,7,10}
a.symmetric_difference_update(b)
a
{1, 2, 8, 9, 10}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,910,11,12}
a.copy()
{1, 2, 3, 4, 5, 6, 7, 8}
a.clear()
a
set()
>>> b=set()
>>> b.add(20,21,30)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    b.add(20,21,30)
TypeError: set.add() takes exactly one argument (3 given)
>>> b.add(23)#only one is possible
>>> 
>>> b
{23}
>>> a={20,30,40}
>>> a.pop(30)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.pop(30)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop(2)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(30)
>>> a
{40, 20}
>>> a={45,23,6,7,89,23}
>>> a.pop()
23
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
True
>>> a.discard(4)
>>> a
{1, 2, 3, 5}
