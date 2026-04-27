Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
>>> a=6
>>> type(a)
<class 'int'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="sindhu"
>>> type(d)
<class 'str'>
>>> e='''hi'''
>>> type(e)
<class 'str'>
>>> f=5+3j
>>> type(f)
<class 'complex'>
>>> z=6j
>>> type(z)
<class 'complex'>
>>> d=8+6i
SyntaxError: invalid decimal literal
>>> y=True
>>> type(Y)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type(Y)
NameError: name 'Y' is not defined. Did you mean: 'y'?
>>> type(y)
<class 'bool'>
>>> s=true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> j="true"
>>> type(j)
<class 'str'>
