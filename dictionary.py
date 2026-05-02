Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"year":2026,"month":5}
print(a)
{'year': 2026, 'month': 5}
type(a)
<class 'dict'>
b={"year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['year', 'month'])
a.values()
dict_values([2026, 5])
a.items()
dict_items([('year', 2026), ('month', 5)])
a.a={"name":"sindhu","mail":"sindhu@gmail.com"}
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.a={"name":"sindhu","mail":"sindhu@gmail.com"}
AttributeError: 'dict' object has no attribute 'a' and no __dict__ for setting new attributes
a={"name":"sindhu","mail":"sindhu@gmail.com"}
a
{'name': 'sindhu', 'mail': 'sindhu@gmail.com'}
a.update({"year":2026},{"month":5})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.update({"year":2026},{"month":5})
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026,"month":5})
a
{'name': 'sindhu', 'mail': 'sindhu@gmail.com', 'year': 2026, 'month': 5}
a={"year":2026,"month":6}
a.setdeafult("date",2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.setdeafult("date",2)
AttributeError: 'dict' object has no attribute 'setdeafult'. Did you mean: 'setdefault'?
a.setdefault("date",2)
2
a
{'year': 2026, 'month': 6, 'date': 2}
#pop()
a.pop()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(year)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop(year)
NameError: name 'year' is not defined
a.pop("year")
2026

a
{'month': 6, 'date': 2}
a.popitem()
('date', 2)

a
{'month': 6}
>>> a={"month":5,"time":1,"sec":4}
>>> a.copy()
{'month': 5, 'time': 1, 'sec': 4}
>>> a["time"]
1
>>> a.get("sec")
4
>>> a
{'month': 5, 'time': 1, 'sec': 4}
>>> b=a
>>> b
{'month': 5, 'time': 1, 'sec': 4}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"course":"python"})
>>> b
{'course': 'python'}
>>> #no duplicates
>>> a={"name":"sindhu","city":"vij","name":"sindhu"}
>>> a
{'name': 'sindhu', 'city': 'vij'}
>>> a={"name":"sindhu","city":"vij","name":"sam"}
>>> a
{'name': 'sam', 'city': 'vij'}
>>> a={"name1":"sindhu","city":"vij","name2":"sindhu"}
>>> a
{'name1': 'sindhu', 'city': 'vij', 'name2': 'sindhu'}
>>> 
>>> a={"idno":[1,2,3],"name":["sam","sindhu","nap"],"marks":[30,70,80]}
>>> a
{'idno': [1, 2, 3], 'name': ['sam', 'sindhu', 'nap'], 'marks': [30, 70, 80]}
>>> a.keys()
dict_keys(['idno', 'name', 'marks'])
>>> a.values()
dict_values([[1, 2, 3], ['sam', 'sindhu', 'nap'], [30, 70, 80]])
>>> a.items()
dict_items([('idno', [1, 2, 3]), ('name', ['sam', 'sindhu', 'nap']), ('marks', [30, 70, 80])])
