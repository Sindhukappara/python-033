#while loop
a=10
while a<1:
    print("true")#empty
    
a=10
while a>1:
    print(a)#infinite 10's


a=20
while a>1:
    print(a)
    a-=1  #20-2
    
a=20
while a>1:
    a-=1
    print(a)#19-1

a=20
while a>4:
    a-=1
    print(a)#19-4

a=10
while a>1:
    print(a)
    a+=1 #10-infinite

a=1
while a<10:
    print(a)
    a+=1  #1-9

a=10
while a>1:
    print(a)
    a-=1 #(10-2)

#while:True
while True:
    age=int(input())
    if age>=18:
        print("They are eligible to vote")
    else:
        print("There are not eligible to vote")

#range()
#start,stop,step
a=20
for i in range(a):
    print(i)

for i in range(1,15):
    print(i)

for i in range(5,26):
    print(i)

#tasks
for i in range(2,20,2):
    print(i,end=" ")


for i in range(0,30,3):
    print(i,end=" ")

for i in range(5,50,5):
    print(i,end=" ")

#task
marks=int(input())
for i in range(91,101):
    if marks==i:
        print("Grade A")
for i in range(81,91):
    if marks==i:
        print("Grade B")
for i in range(71,81):
    if marks==i:
        print("Grade C")
for i in range(50,71):
    if marks==i:
        print("Grade D")
for i in range(0,50):
    if marks==i:
        print("Fail")

while True:
    marks=int(input())
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")
    


#break
a=30
while a>5:
    print(a)
    a-=1
    if a==15:
        break #30-16

a=30
while a>5:
    a-=1
    if a==15:
        break
    print(a)#29-16


for i in range(19):
    if i==10:
        break
    print(i)#0-9


for i in range(19):
    if i==10:
        break
print(i)#10


a="python"
for i in a:
    if i=="h":
        break
    print(i)#pyt

#continue
a=20
while a>1:
    print(a)
    a-=1
    if a==10:
        continue #does not skip
a=20
while a>1:
    a-=1
    if a==10:
        continue
    print(a)  #skips 12

for i in range(19):
    if i==11:
        continue
    print(i)


a="python"
for i in a:
    if i=="y":
        continue
    print(i)


#pass
a=10
while a>1:
    print(a)
    a-=1
    if a==5:
        pass

for i in range(5):
    if i==2:
        pass
    print(i)
    
    


















    

















    
    
