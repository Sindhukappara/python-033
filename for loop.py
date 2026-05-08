#loops
'''
a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))
#list

a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))

a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")

#tuple
a=(1,2,3,4,5,6)
for i in a:
    print(i)
    print(type(a))
    print(type(i))
#set
a={4,5,6,7,8,9}
for i in a:
    print(i)
    print(type(a))
    print(type(i))

#dict
a={"year":2026,"month":5,"date":7}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))


a="codegnan"
for i in a:
    print(i)

a="codegnan"
for i in a:
    print(i,end=" ")
    print(type(a))
    print(type(i))
    

a=["apple","banana","grapes"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))

a=[3,6.5,"apple",8+9j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))

'''

#Task 1
a=["codegnan","python","course"]
'''
#method 1
for i in a:
    print(i.upper(),end=",")
    
#method 2
b=str(a)
c=b.upper()
print(c)

#method 3
b=[]
for i in a:
    b.append(i.upper())
print(b)
    
'''




















   


    












