# 1
def pri():
    i = 0
    while i < 10:
        print("softwarica")
        i += 1
pri()

# 2
l = [1, 2, 3, 4]
def sum(a):
    s = 0
    i = 0
    while i < len(a):
        s = s + a[i]
        i += 1
    print(s)
sum(l)

# 3
def char(a):
    i = 0
    while i < len(a):
        print(a[i])
        i += 1
char("hello")

# 4
a = [1, "a", "c", 2, 3, 4]
def tp():
    i = 0
    while i < len(a):
        if type(a[i]) == int:
            print(a[i])
        i += 1
tp()

# 5
l = [4, 5, 3, 2]
mul = 1
def multiply(a, p):
    i = 0
    while i < len(a):
        p *= a[i]
        i += 1
    return p
print(multiply(l, mul))

# 6
a = int(input("Any number for multiplication table: "))
def tab(t):
    i = 1
    while i < 11:
        s = t * i
        print("{}*{} = {}".format(t, i, s))
        i += 1
tab(a)

# 7
a = [1, "a", "c", 2, 3, 4]
def rev(l):
    i = len(l) - 1
    while i >= 0:
        print(l[i])
        i -= 1
rev(a)

# 8
a = [1, 2, 3, 4]
b = []
def inc(l, k):
    i = 0
    while i < len(l):
        r = l[i] + 1
        k.append(r)
        i += 1
    return k
print(inc(a, b))

# 9
a = int(input("Give any number: "))
def prm(x):
    p = 0
    i = 1
    while i <= x:
        if x % i == 0:
            p += 1
        i += 1
    if p == 2:
        print("It is a prime number.")
    else:
        print("It is not prime.")
prm(a)

# 10
a = int(input("Give a range to find prime number: "))
def rprm(x):
    p = 0
    i = 1
    while i <= x:
        if x % i == 0:
            p += 1
        i += 1
    return p
def prm(b):
    i = 1
    while i <= b:
        c = rprm(i)
        if c == 2:
            print(i)
        i += 1
prm(a)

# 11
a = input("Enter a string: ")
b = 0
c = 0
d = 0
def cou(string, digits, letters, spaces):
    i = 0
    while i < len(string):
        if string[i].isdigit():
            digits += 1
        elif string[i].isalpha():
            letters += 1
        elif string[i].isspace():
            spaces += 1
        i += 1
    print("Number of digits:", digits)
    print("Number of letters:", letters)
    print("Number of spaces:", spaces)
cou(a, b, c, d)

# 12
max_try = 3
def check(x):
    i = 1
    while i <= x:
        a = input("Enter username: ")
        b = input("Enter password: ")
        if b.isalnum() and len(a) >= 5 and len(b) >= 5:
            print("Username and password are valid.")
            break
        else:
            print("Username and password are invalid. Please try again.")
        if i == x:
            print("Maximum attempts reached. Exiting....")
        i += 1
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
n = int(input("Enter a number: "))
def fac(a):
    f = 1
    i = 1
    while i <= a:
        f *= i
        i += 1
    return f
print("Factorial is ", fac(n))

# 15
num = int(input("Enter a number: "))
def pal(n):
    a = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev
if num == pal(num):
    print("Palindrome")
else:
    print("Not Palindrome")

# 16
n = int(input("Enter a number: "))
def arm(a):
    b = a
    s = 0
    while a > 0:
        c = b % 10
        s += c ** len(str(a))
        b = b // 10
    return s
if n == arm(n):
    print("Armstrong")
else:
    print("Not Armstrong")

# 17
n = int(input("Enter a number: "))
import math as m
def ps(a):
    x = 1
    i = 0
    while i < 2:
        x = x * (m.sqrt(a))
        i += 1
    return x
if n == ps(n):
    print("Perfect Square")
else:
    print("Not Perfect Square")

# 18
n = int(input("Enter a number: "))
def pn(a):
    s = 0
    i = 1
    while i < a:
        if a % i == 0:
            s += i
        i += 1
    return s
if n == pn(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")

# 19
def n1(a):
    i = 1
    while i <= 10:
        s = a * i
        print("{}*{} = {}".format(a, i, s))
        i += 1
def m():
    i = 1
    while i <= 8:
        n1(i)
        print()
        i += 1
m()

# 20
lst = [1, 2, 3, 4]
def p(a):
    l = []
    i = 0
    while i < len(a):
        if a[i] < 3:
            l.append(a[i])
        i += 1
    return l
print(p(lst))

# 21
r1 = int(input("Enter a range from: "))
r2 = int(input("to: "))
def ran(a, b):
    s = 0
    i = a
    while i < b:
        if i % 2 == 1:
            s += i
        i += 1
    return s
print("The sum of all odd numbers in the range {} to {} is {}".format(r1, r2, ran(r1, r2)))

# 22
r1 = int(input("Enter a range from: "))
r2 = int(input("to: "))
def ran(a, b):
    s = 0
    i = a
    while i < b:
        if i % 2 == 0:
            s += i
        i += 1
    return s
print("The sum of all even numbers in the range {} to {} is {}".format(r1, r2, ran(r1, r2)))

# 23
string = input("Enter a String: ")
def cou(s):
    a = 0
    i = 0
    while i < len(s):
        if s[i].isspace():
            a += 1
        i += 1
    return a
print(cou(string))

# 24
lst = [1, 2, 3, 4]
def ch(l):
    a = []
    i = 0
    while i < len(l):
        a.append(l[i] ** 3)
        i += 1
    print(a)
ch(lst)

# 25
list = input("Enter a list of numbers separated by spaces: ").split()
def prod(num):
    a = [int(i) for i in num]
    p = 1
    i = 0
    while i < len(a):
        p *= a[i]
        i += 1
    return p
print("Product is:", prod(list))

# 26
a=0
def rang(i):
    while i < 50:
        if i == 8:
            break
        print(i)
        i+=1
rang(a)

# 27
s = input("Enter a string: ")
def pri(a):
    i = 0
    while i < len(a):
        print(a[i])
        i += 1
pri(s)

# 28
l = ["ram", "shyam", 1, 2]
def pli():
    i = 0
    while i < len(l):
        if type(l[i]) == str:
            print("Hello!" + l[i], end=" ")
        i += 1
pli()

# 29
l = ["ram", "shyam", 1, 2]
def prin(a):
    lst = []
    i = 0
    while i < len(a):
        lst.append("Dr." + str(a[i]))
        i += 1
    return lst
print(prin(l))

# 30
list = input("Enter a list of numbers separated by spaces: ").split()
def prod(num):
    a = [int(i) for i in num]
    p = 1
    i = 0
    while i < len(a):
        p *= a[i]
        i += 1
    return p
print("Product is:", prod(list))

# 31
lst = [111, 32, -9, -45, -17, 9, 85, -10]
l = []
def app(a):
    i = 0
    while i < len(a):
        if a[i] > 0:
            l.append(a[i])
        i += 1
    return l
print(app(lst))

# 32
l = [0, 1, 2, 3, 4, 5, 6]
nl = []
def exp(a, b):
    i = 0
    while i < len(a):
        if a[i] == 3 or a[i] == 6:
            i += 1
            continue
        b.append(a[i])
        i += 1
    return b
print(exp(l, nl))

# 33
l = [1, (2, 3), "abhishek", 2.1, True, (1, 2)]
nl = []
def copy(a):
    i = 0
    while i < len(a):
        nl.append(type(a[i]))
        i += 1
    print(nl)
copy(l)

# 34
def exec():
    i = 0
    while i < 7:
        print(i)
        i += 1
    else:
        print("Done")
exec()

# 35
def ser():
    i = 105
    while i >= 0:
        print(i, end=" ")
        i -= 7
ser()

# 36
s = "py;th* o:n ! ;py * t*h:o !n"
b = [';', ':', '!', '*']
n = ""
def bst(a, b, c):
    i = 0
    while i < len(a):
        if a[i] not in b and a[i] != " ":
            c += a[i]
        i += 1
    return c
print(bst(s, b, n))

# 37
series = input("Enter a list of numbers separated by spaces: ").split()
a = [int(i) for i in series]
def odev(n):
    o = 0
    e = 0
    b = []
    i = 0
    while i < len(n):
        if n[i] % 2 == 0:
            e += 1
        else:
            o += 1
        i += 1
    b.append(o)
    b.append(e)
    return b
b = odev(a)
print("Numbers of even numbers is", b[1])
print("Numbers of odd numbers is", b[0])

# 38
lst = [1, 2, 3, 4]
def a(p):
    i = 0
    while i < len(p):
        if p[i] != 3:
            print(p[i])
        i += 1
a(lst)

# 39
lst=[1,2,3,4]
def a(p):
    i = 0
    while i < len(p):
        if p[i] != 3 and p[i]!=2:
            print(p[i])
        i += 1
a(lst)

# 40
list = [1, 2, 3, 4]
def rep(lst):
    i=1
    while i < len(lst):
        if i == 1:
            lst[i] = "a"
        elif i == 2:
            lst[i] = 2
        i += 1
    return(lst)
print(rep(list))
