#Conditions
#if condition using comparision operator
#<,>,<=,>=,!=,==
a=4
b=8
if a>b:
    print("True")
    
a=4
b=8
if a<b:
    print("True")

a=4
b=8
if a>=b:
    print("True")

a=4
b=8
if a<=b:
    print("True")

a=6
b=7
if a!=b:
    print("Not Equal")
    
a=7
b=7
if a==b:
    print("Equal")

a=int(input())
b=int(input())
if a>b:
    print("True")

a=int(input())
if a>7:
    print("hi")


a="python"
if a=="python":
    print("it is true")

a=input()
if a=="java":
    print("Equal")

#if condition by using logical operators
#and,or,not

a=7
b=8
if a<b and b>a:
    print("True")

a=7
b=8
if a<=b and b>=a:
    print("True")

a=5
b=10
if a!=b and b==a:
    print("True")

a=7
b=8
if a<b or b>a:
    print("True")

a=7
b=8
if a>b or b>a:
    print("True")

a=5
b=8
if a>=b or  b>=a:
    print("True")

a=6
b=7
if not a<b:
    print("True")

a=8
b=9
if not a>b:
    print("True")

a=6
b=5
if a!=b or b==a:
    print("True")

#if condition by identifier operators
# is, is not

a=6
if type(a) is int:
    print("it is int")


a=6
if type(a) is not int:
    print("it is int")

a=int(input())
if type(a) is int:
    print("true")
    
    
a=int(input())
if type(a) is not int:
    print("true")

#str

a="sindhu"
if type(a) is str:
    print("it is str")

a="sindhu"
if type(a) is not str:
    print("it is str")

a=input()
if type(a) is str:
    print("it is str")


a=input()
if type(a) is not str:
    print("it is str")

#if condition by membership
#in,not in

a=[10,20,30,40,50]
if 50 in a:
    print("yes")

a=[10,20,30,40,50]
if 50 not in a:
    print("yes")

a=[10,20,30,40,50]
if 70 not in a:
    print("yes")

a=int(input())
if 60 in a:
    print("true")#error

a=[10,20,56,46,30]
b=int(input())
if b in a:
    print("yes")

#if-else conditions by using comparision operators

a=3
b=6
if a<b:
    print("less")
else:
    print("not less")

a=3
b=6
if a>b:
    print("less")
else:
    print("not less")
    
#logical
a=7
b=8
if a<b and b>a:
    print("True")
else:
    print("False")

a=7
b=8
if a<=b and b>=a:
    print("True")
else:
    print("False")

a=5
b=10
if a!=b and b==a:
    print("True")
else:
    print("False")

a=7
b=8
if a<b or b>a:
    print("True")
else:
    print("False")

a=7
b=8
if a>b or b>a:
    print("True")
else:
    print("False")

a=5
b=8
if a>=b or  b>=a:
    print("True")
else:
    print("False")

#if condition using identifier
a=6
if type(a) is int:
    print("it is int")
else:
    print("it is not int")


a=6
if type(a) is not int:
    print("it is int")
else:
    print("it is not int")


a=int(input())
if type(a) is int:
    print("true")
else:
    print("it is not int")
    
    
a=int(input())
if type(a) is not int:
    print("true")
else:
    print("it is not int")

#membership operator
#in,not in
a=[10,20,30,40,50]
if 50 in a:
    print("yes")
else:
    print("No")

a=[10,20,30,40,50]
if 50 not in a:
    print("yes")
else:
    print("No")

a=[10,20,30,40,50]
if 70 not in a:
    print("yes")
else:
    print("No")

a=int(input())
if 60 in a:
    print("true")
else:
    print("No")#error

a=[10,20,56,46,30]
b=int(input())
if b in a:
    print("yes")
else:
    print("No")

#if-elif-else
a=4
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")
    

a=4
b=8
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")

a=4
b=8
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")


a=4
b=8
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a==b:
    print("equal")
else:
    print("true")

#logical
a=7
b=8
if a<b and b>a:
    print("True")
elif a==b:
    print("Equal")
else:
    print("False")


a=7
b=7
if a>b and b>a:
    print("True")
elif a==b:
    print("Equal")
else:
    print("False")

a=7
b=8
if a>b and b>a:
    print("True")
elif a==b:
    print("Equal")
else:
    print("False")

a=6
b=4
if a>b or a<b:
    print("True")
elif a==b:
    print("Equal")
else:
    print("False")

#identifier
a=6
if type(a) is int:
    print("it is int")
elif type(a) is float:
    print("it is float")
else:
    print("it is not int")


a=6.6
if type(a) is int:
    print("it is int")
elif type(a) is float:
    print("it is float")
else:
    print("other data type")

a=input()
if type(a) is int:
    print("it is int")
elif type(a) is float:
    print("it is float")
else:
    print("date type",type(a))

#membership operator
a=[10,20,30,40,50]
if 50 not in a:
    print("yes")
elif 30 in a:
    print("it is present")
else:
    print("No")

#multiple if
a=8
b=10
if a<b:
    print("Less")
if b>a:
    print("greater")
if a!=b:
    print("true")
    

a=8
b=10
if a==b:
    print("Less")
if b>a:
    print("greater")
if a!=b:
    print("true")

#logical
a=7
b=8
if a<b and b>a:
    print("True")
if a==b:
    print("Equal")
if a<b or a>b:
    print("False")

#identifier
a=input()
if type(a) is int:
    print("date type",type(a))
if type(a) is float:
    print("date type",type(a))
if type(a) is str:
    print("date type",type(a))
#membership

a=[10,20,30,40,50]
if 50 not in a:
    print("yes")
if 30 in a:
    print("it is present")
if 20 in a:
    print("yes")

#nested if conditions
a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")

a=5
b=10
if a<b:
    print("less")
    if b==a:
        print("greater")


a=5
b=10
if a>b:
    print("less")
    if b>a:
        print("greater")

a=5
b=10
if a<b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")


a=5
b=10
if a>b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
        print("true")
else:
    print("the number is less")

    

a=5
b=10
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
        print("true")
    else:
        print("it is true")
else:
    print("the number is less") 



    


    
    
    






    















    


    



