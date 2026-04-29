Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Vijayawada"
a[1]
'i'
a[0]
'V'
a[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[10]
IndexError: string index out of range
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Vijaya'
a="i am a girl"
a[0]
'i'
a[1]+a[4]+a[6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[1]+a[4]+a[6]
'   '
a[7]+a[8]+a[9]+a[10]
'girl'
a="i love python"
a[2]+a[3]+a[4]+a[5]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'lovepython'
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]+a[11]+a[12]+a[22]+a[23]+a[24]+a[25]
'royaliscity'
a[16]+a[17]+a[18]+a[19]+a[20]+a[22]+a[23]+a[24]+a[25]+a[11]+a[12]
'royalcityis'
#Indexing

#negative indexing
a="hi sindhu"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'sindhu'
a[-9]+a[-8]
'hi'
#slicing
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a[0:3]
'cod'
a="work hard until you succeed"
a[22:]
'cceed'
a[21:]
'ucceed'
a[23:]
'ceed'
a[20:]
'succeed'
a[11:16]
'ntil '
a[10:16]
'until '
a[6:10]
'ard '
a[5:10]
'hard '
a[:4]
'work'
a[17:20]
'ou '
a[16:20]
'you '
b="i am learning python course"
b[2:4]
'am'
b[5:13]
'learning'
b[5:10]
'learn'
b[13:19]
' pytho'
b[14:20]
'python'
b[21:27]
'course'
#negative slicing
a="simple is better than complex"
a[-7:-1]
'comple'
a[-7:]
'complex'
a[-19:-13]
'better'
a[-29:-23]
'simple'
a="beautiful is better than ugly"
a[-29:-20]
'beautiful'
a[-4:]
'ugly'
a[-19:-17]
'is'
#striding
a="cloud computing"
>>> a[::5]
'c u'
>>> a[:6]
'cloud '
>>> a[8:]
'mputing'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[::7]
'cog'
>>> a[::1]
'cloud computing'
>>> a[5:12]
' comput'
>>> b="machine learning"
>>> b[2:11:3]
'cnl'
>>> b[3:15:4]
'h r'
>>> b[5:12:2]
'n er'
>>> b[1:10:5]
'ae'
>>> a="python course"
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-6]
'uh'
>>> a[-3:-9:-2]
'ro '
>>> #rules
>>> a[7:4:2] #highest to lowest not possible
''
>>> a[-9:-5:-2]#in negative lowest to highest not possible
''
>>> a[::-1]
'esruoc nohtyp'
