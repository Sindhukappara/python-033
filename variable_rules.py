Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=3
print(a+b)
5
print(7+9)
16
print(10+10)
20
x=10
print(x)
10
Y=45
print(Y)
45
print(Z)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined
print(z)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
print(X)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
10
9a=6
SyntaxError: invalid decimal literal
3=6
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
_a=6
print(_a)
6
_=4
print(_)
4
@=6
SyntaxError: invalid syntax
_@=7
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    _@=7
TypeError: unsupported operand type(s) for @=: 'int' and 'int'
name="sindhu"
print(name)
sindhu
print("name")
name
country="India"
print(country)
India
TypeError: unsupported operand type(s) for @=: 'int' and 'int'
SyntaxError: invalid syntax
if=6
SyntaxError: invalid syntax
for=67
SyntaxError: invalid syntax
#keywords cannot be used
a=5,b=6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=5;b=6
>>> a,b=5,6
>>> print(a+b)
11
>>> first name=sindhu
SyntaxError: invalid syntax
>>> first name="sindhu"
SyntaxError: invalid syntax
>>> first_name="sindhu"
>>> last_name="kappara"
>>> print(first_name+last_name)
sindhukappara
>>> #for space between words
>>> print(first_name,last_name)
sindhu kappara
>>> #or
>>> print(first_name+" "+last_name)
sindhu kappara
>>> #Case Sensitive
>>> age=7
>>> print(age)
7
>>> Age=67
>>> print(Age)
67
>>> AGE=78
>>> print(AGE)
78
>>> #del keyword
>>> a=7
>>> print(a)
7
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
