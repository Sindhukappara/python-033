Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a//2)
1
print(a/2)
1.0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment
a=6
b=4
b+=a
b
10
b-=a
b
4
b*=a
b
24
b//=a
b
4
b/=a
b
0.6666666666666666
b=5
b**=a
b
15625
b%=a
b
1
print(a+=b)
SyntaxError: invalid syntax
#comparision operator





a=6
b=7
a>b
False
a<b
True
a>=b
False
a<=b
True
a!=b
True
a==b
False
#logical
a=6
b=3
a>b and b<a
True
a<b and b>a
False
a<=b and b>=a
False
a=5
b=9
a>b or b>a
True
a<b or b>a
True
a>b or b<a
False
a!=b and a==b
False
a!=b or a==b
True
not True
False
not False
True
#Identity Operator
a=6
if type(a) is int:
    print("true")

    
true
if type(a) is not int:
    print("it is not int")

    
b=6.4
if type(b) is float:
    print("True")

    
True
if type(b) is not float:
    print("hi")

#membership operator
    
a=4,5,6,3,6,7,3,10,4,11
if 10 in a:
    print(10)

    
10
>>> if 3 in a:
...     print(4)
... 
...     
4
>>> if 13 in a:
...     print(5)
... 
...     
>>> #bitwise
...     
>>> a=6
>>> b=4
>>> bin(6)
'0b110'
>>> bin(7)
'0b111'
>>> bin(4)
'0b100'
>>> a&b
4
>>> a|b
6
>>> a=6
>>> ~a
-7
>>> #xor
>>> a=6
>>> b=2
>>> a^b
4
>>> #<<
>>> a=4
>>> a<<3
32
>>> #a=6
>>> a=6
>>> a>>2
1
