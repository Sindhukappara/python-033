#run_time input()
a=int(input("enter the value:"))
b=int(input("enter the value:"))
print(a+b)

#float

a=float(input("enter the value:"))
b=float(input("enter the value:"))
print(a+b)

#int
a=int(input("enter the value:"))
b=int(input("enter the value:"))
print(a+b)

#string

a=str(input("enter the value:"))
b=str(input("enter the value:"))
print(a+" "+b)

#complex

a=complex(input("enter the value:"))
b=complex(input("enter the value:"))
print(a+b)

#boolean

a=bool(input("enter the value:"))
b=bool(input("enter the value:"))
print(a+b)

a=bool(input("enter the value:"))
b=bool(input("enter the value:"))
c=bool(input("enter the value:"))
print(a+b+c)

#runtime in multiple lines

a=int(input("enter your value:"))
b=int(input("enter your value:"))
option=int(input("select your operation : 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a/b) 

a=int(input("enter your value:"))
b=int(input("enter your value:"))
option=int(input("select your operation :
                 1.add
                 2.sub
                 3.mul"))
print(a+b)
print(a-b)
print(a/b)


a=int(input("enter your value:"))
b=int(input("enter your value:"))
option=input("select your operation : 1.add 2.sub 3.mul")
print(a+b)
print(a-b)
print(a/b)

#method1

a=int(input("enter the number"))
b=int(input("enter the number"))
a,b=b,a
print(a,b)
                 
#method2

a=int(input("enter the number"))
b=int(input("enter the number"))
temp=a
a=b
b=temp
print(a,b)

#method3

a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b)

#method4(number formating)
#int
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))
#float
a=float(input())
b=float(input())
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" %(a,b))
                 
#string

a=str(input())
b=str(input())
a,b=b,a
print("after swapping a=%s,b=%s" %(a,b))

















