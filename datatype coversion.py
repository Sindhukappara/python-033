Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(8)
8
int(8.0)
8
int("sindhu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("sindhu")
ValueError: invalid literal for int() with base 10: 'sindhu'
int(5+3j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
float(6.7)
6.7
float("sindhu")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("sindhu")
ValueError: could not convert string to float: 'sindhu'
float(5+6j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(1)
'1'
str(1.0)
'1.0'
str("sindhu")
'sindhu'
str(5+6j)
'(5+6j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(1)
(1+0j)
>>> complex(5.0)
(5+0j)
>>> comlex("sindhu")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    comlex("sindhu")
NameError: name 'comlex' is not defined. Did you mean: 'complex'?
>>> complex("sindhu")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("sindhu")
ValueError: complex() arg is a malformed string
>>> complex(5+6j)
(5+6j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(1)
True
>>> bool(1.0)
True
>>> bool("sindhu")
True
>>> bool(5+6j)
True
>>> bool(True)
True
>>> bool(False)
False
