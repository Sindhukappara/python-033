Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
###len()

 #count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("n")
2
a.count("star")
1
a.count("t")
5
#find()
a="coding"
a.find("i")
3
a="hello"
find("l")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    find("l")
NameError: name 'find' is not defined
a.find("l")
2
#if it is repeated then it gives only the first starting index

 #escape sequences
#\n->new line
#\t->
#tab space
a="name\nmobileno\temail"
print(a)
name
mobileno	email
b="sindhu\n mobileno:567467\temail:abc@gmail.com"
print(b)
sindhu
 mobileno:567467	email:abc@gmail.com

#replace()
 
a="wait until you succeed wait"
a.replace("wait","work")
'work until you succeed work'

a.replace("i","j")
'wajt untjl you succeed wajt'

a="sindhu"
a.upper()
'SINDHU'
 a="PYTHON"
 
SyntaxError: unexpected indent
a="PYTHON"
a.lower()
'python'
a.captalize()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a.capitalize()
'Python'
a="python course"
a.capitalize()
'Python course'
a.title()
'Python Course'
b="i am a good girl"
b.title()
'I Am A Good Girl'

a="data"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="5647"
b.isdigit()
True
b.isnumeric()
True
c="sindhu123"
c.isalnum()
True
a="python course"
a.isalpha()
False
a="7.6"
a.isdigit()
False
a.isnumeric()
False
b="8.65656"
b.isdecimal()
False
b="7"
b.isdecimal()
True\

#concat
a="sindhu"
b="kappara"
print(a+b)
sindhukappara
print(a+" "+b)
sindhu kappara
print(a.title()+" "+b.title())
Sindhu Kappara
print((a+" "+b).title())
Sindhu Kappara

#strip()
#lstrip(),rstrip()
a="      sindhu    "
a.strip()
'sindhu'
a.lstrip()
'sindhu    '
a.rstrip()
'      sindhu'

#split()
a="python c c++ java"
a.split()
['python', 'c', 'c++', 'java']
b="i am a learning python full stack"
b.split()
['i', 'am', 'a', 'learning', 'python', 'full', 'stack']

#join()

a="apple","mango","banana"
"".join(a)
'applemangobanana'
" ".join(a)
'apple mango banana'
b="apple"," ","mango"
"k".join(a)
'applekmangokbanana'
" ".join(b)
'apple   mango'

a=5
b=9
print(a+b)
14
#formatting
print("the sum is :",a+b)
the sum is : 14
print("the sum is a+b")
the sum is a+b
city="vij"
print("the city is",city)
the city is vij

#format method
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> print("hello {}hello {}".format(a,b))
hello motuhello patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> #fstring
>>> a="choota"
>>> b="bheem"
>>> print(f"hello {a}{b}")
hello chootabheem
>>> print(f"hello {a} {b}")
hello choota bheem
>>> print(f"hello {a} hello {b}")
hello choota hello bheem
>>> 
>>> #multiplication of 11
>>> a=11
>>> b=2
>>> print("{} {}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print("{} {}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("multiplication {}{}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print("multiplication {}{}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("{} {}".format(a,b))
11 2
>>> print("{}*{}".format(a,b),a*b)
11*2 22
>>> print("{}*{}=".format(a,b),a*b)
11*2= 22
>>> print(f"{a} {b}",a*b)
11 2 22
>>> print(f"{a}*{b}=",a*b)
11*2= 22
