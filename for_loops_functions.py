# 1
def pri ():
    for i in range (10) :
        print("softwarica")
pri()

# 2
l=[1,2,3,4]
def sum(a):
    s=0
    for i in range (len(a)):
        s=s+a[i]
    print (s)
sum(l)

# 3
def char(a):
    for i in range (len(a)):
        print(a[i])
char("hello")

# 4
a=[1,"a","c",2,3,4]
def tp ():
    for i in range (len(a)):
        if type(a[i])== int:
            print(a[i])
tp()

# 5
l=[4,5,3,2]
mul=1
def multiply(a,p):
    for i in a:
        p*=i
    return(p)
print(multiply(l,mul))

# 6
a=int(input("Any number for multiplication table: "))
def tab (t):
    for i in range (1,11):
        s= t* i
        print("{}*{} = {}".format(t,i,s))
tab(a)

# 7
a=[1,"a","c",2,3,4]
def rev(l):
    r=[]
    for i in reversed(range (len(l))):
        r.append(a[i])
    print(r)
rev(a) 

# 8
a=[1,2,3,4]
b=[]
def inc(l,k):
    for i in range(len(l)):
        r=a[i]+1
        k.append(r)
    return(k)
print(inc(a,b))

# 9
a=int(input("Give any number: "))
def prm(x):
    p=0
    for i in range(1,x+1):
        if x%i==0:
            p=p+1
    if p==2:
        print("It is a prime number.")
    else:
        print("It is not prime.")
prm(a)

# 10
a=int(input("Give a range to find prime number: "))
def rprm(x):
    p=0
    for i in range (1,x+1):
        if x%i==0:
            p=p+1
    return(p)
def prm(b):
    for i in range(1,b+1):
        c= rprm(i)
        if c==2:
            print (i)
prm(a)



# 11
a = input("Enter a string: ")
b = 0
c = 0
d = 0
def cou (string,digits,letters,spaces):
    for char in string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        elif char.isspace():
            spaces += 1
    print("Number of digits:", digits)
    print("Number of letters:", letters)
    print("Number of spaces:", spaces)

cou(a,b,c,d)

# 12
max_try=3
def check(x):
    for i in range (1,x+1):
        a = input("Enter username: ")
        b = input("Enter password: ")    
        if b.isalnum() and len(a) >= 5 and len(b) >= 5:
            print("Username and password are valid.")
            break
        else:
            print("Username and password are invalid. Please try again.")
        if i==x:
            print("Maximum attempsts reached.Exiting....")
check(max_try)

# 13
number = int(input("Enter a number: "))
def num(a):
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
num(number)

# 14
n= int(input("Enter a number: "))
def fac(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return(f)
print("Factorial is ",fac(n))        

# 15
num = int(input("Enter a number: "))
def pal(n):
    a = n
    rev = 0
    for i in range(len(str(n))):
        rev = rev * 10 + a % 10
        a = a//10
    return(rev)
if num == pal(num):
    print("Palindrome")
else:
    print("Not Palindrome")

# 16
n=int(input("Enter a number: "))
def arm(a):
    b=a
    s=0
    for i in range(len(str(a))):
        c=b%10
        s=s+c**len(str(a))
        b=b//10
    return(s)
if n==arm(n):
    print("Armstrong")
else:
    print("Not Armstrong")

# 17
n=int(input("Enter a number: "))
import math as m
def ps(a):
    x=1
    for i in range (2):
        x=x*(m.sqrt(a))
    return (x)
if n==ps(n):
    print("Perfect Square")
else:
    print("Not Perfect Square")

# 18
n=int(input("Enter a number: "))
def pn(a):
    s=0
    for i in range (1,a):
        if a%i==0:
            s=s+i
    return(s)
if n==pn(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")

# 19
def n1(a):
    for i in range (1,11):
        s= a* i
        print("{}*{} = {}".format(a,i,s))
def m():
    for i in range (1,9):
        n1(i)
        print()
m()

# 20
lst=[1,2,3,4]
def p(a):
    l=[]
    for i in range (len(a)):
        if a[i]<3:
            l.append(a[i])
    return(l)
print(p(lst))

# 21
r1=int(input("Enter a range from: "))
r2=int(input("to: "))
def ran(a,b):
    s=0
    for i in range (a,b):
        if i%2==1:
            s+=i
    return (s)
print("The sum of all odd number in range {} to {} is {}".format(r1,r2,ran(r1,r2)))

# 22
r1=int(input("Enter a range from: "))
r2=int(input("to: "))
def ran(a,b):
    s=0
    for i in range (a,b):
        if i%2==0:
            s+=i
    return (s)
print("The sum of all even number in range {} to {} is {}".format(r1,r2,ran(r1,r2)))

# 23
string=input("Enter a String: ")
def cou(s):
    a=0
    for char in s:
        if char.isspace():
            a+=1
    return(a)
print(cou(string))

# 24
lst=[1,2,3,4]
def ch(l):
    a=[]
    for i in l:
        a.append(i**3)
    print(a)
ch(lst)

# 25
list=input("Enter a list of numbers separated by spaces: ").split()
def prod(num):
    a=[int(i) for i in num]
    p=1
    for i in a:
        p*=i
    return(p)
print("Product is:", prod(list))

# 26
def rang():
    for i in range(50):
        if i==8:
            break
        print(i)
rang()

# 27
s=input("Enter a string: ")
def pri(a):
    for i in a:
        print(i)
pri(s)

# 28
l=["ram", "shyam", 1, 2]
def pli():
    for i in l:
        if type(i)==str:
            print("Hello!"+i,end=" ")
pli()

# 29
l=["ram", "shyam", 1, 2]
def prin(a):
    lst=[]
    for i in a:
        lst.append("Dr." + str(i))
    return(lst)
print(prin(l))

# 30
list=input("Enter a list of numbers separated by spaces: ").split()
def prod(num):
    a=[int(i) for i in num]
    p=[]
    for i in a:
       p.append(i**2) 
    return(p)
print("Product is:", prod(list))

# 31
lst = [111, 32, -9, -45, -17, 9, 85, -10]
l = []
def app(a):
    for i in a:
        if i > 0:
            l.append(i)
    return(l)
print(app(lst))

# 32
l=[0,1,2,3,4,5,6]
nl=[]
def exp(a,b):
    for i in range (len(a)):
        if a[i]==3 or a[i]==6:
            continue
        b.append(a[i])
    return(b)
print(exp(l,nl))

# 33
l = [1,(2,3), "abhishek", 2.1, True, (1,2)]
nl = []
def copy(a):
    for i in a:
     nl.append(type(i))
    print(nl)    
copy(l)

# 34
def exec():
    for i in range(7):
        print(i)
    else:
        print("Done")
exec()

# 35
def ser():
    for i in range(105,0,-7):
        print(i,end=" ")
ser()

# 36
s="py;th* o:n ! ;py * t*h:o !n"
b=[';', ':', '!', '*']
n=""
def bst(a,b,c):
    for i in a:
        if not b.__contains__(i) and i !=" ":
            c += i
    return(c)
print(bst(s,b,n))

# 37
series=input("Enter a list of numbers separated by spaces: ").split()
a=[int(i) for i in series]
def odev(n):
    o=0
    e=0
    b=[]
    for i in n:
        if i%2==0:
            e+=1
        else:
            o+=1
    b.append(o)
    b.append(e)
    return(b)
b=odev(a)
print("Numbers of even number is ",b[1])
print("Numbers of oddd number is ",b[0])

# 38
lst=[1,2,3,4]
def a(p):
    for i in p:
        if i!=3:
            print(i)
a(lst)

# 39
lst=[1,2,3,4]
def a(p):
    for i in p:
        if i!=3 and i!=2:
            print(i)
a(lst)

# 40
list = [1, 2, 3, 4]
def rep(a):
    for i in range(1,len(a)):
        if i == 1:
            a[i]="a"
        elif i ==2:
            a[i]=2  
    return(a) 
print(rep(list))        

    
