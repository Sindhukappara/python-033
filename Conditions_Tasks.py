#voting
#task 1

age=int(input())
if age>=18:
    print("They are eligible to vote")
else:
    print("There are not eligible to vote")
    
#task 2 (even or odd)
n=int(input())
if n%2==0:
    print("it is even")
else:
    print("it is odd")
    
#task 3(leap year or not)
year=int(input())
if year%4==0:
    print("it is leap year")
else:
    print("it is not leap year")

#task 4
n=input()
if n in 'a''e''i''o''u':
    print("vowel")
else:
    print("consonent")

#task 5

n=input()
if n=="sindhu":
    print("Welcome",n)
elif n=="yesaswini":
    print("Welcome",n)
elif n=="Mercy":
    print("Welcome",n)
elif n=="somu":
    print("Welcome",n)
elif n=="saara":
    print("Welcome",n)
else:
    print("Welcome Guest")


n=["sindhu","yesaswini","mercy","somu","saara"]
a=input().lower()
if a in n:
    print("Welcome",a)
else:
    print("Welcome guest")
 
#task 6 
#social media login

username,password
if it is a match->successful
if it is not->in valid

#nested if

n=input()
p=input()
if n=='sindhu':
    if p=="1234":
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")

#if-else

n=input()
p=input()
if n=="sindhu" and p=="123":
    print("login successful")
else:
    print("login failed")

#task 7

n=int(input("enter the cake price))
if n==1200:
      print("Red vevlet cake")
elif n==1000:
    print("chocolate cake")
elif n==800:
    print("Almond cake")
elif n==600:
    print("butterscotch cake")
elif n==400:
    print("normal cake")
else:
    print("sorry cake is not available")


#task 8
p=input("enter the pizza name: ")
if p=="bbq":
    print("1000/-")
elif p=="crispy chicken pizza":
    print("800/-")
elif p=="panner pizza":
    print("600/-")
elif p=="corn pizza":
    print("400/-")
elif p=="french fries & coke":
    print("200/-")



