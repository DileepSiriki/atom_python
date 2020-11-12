class MyClass():
     def __init__(self):
             self.__superprivate = "Hello"
             self._semiprivate = ", world!"

mc = MyClass()
print(mc._MyClass__superprivate)
print(mc.__dict__)
print(mc._semiprivate)
print(dir(mc))


mes="dil"
print('mes''eep')
print("mes")

name="dILleep"
#print(title(name))
print("kohIl".title())

print("dileep")
x="io"
print(f"{x.title()}")

print("hi",2+3)

print(2,"hi",5mi)

l=[1,2,3]
print(l[2.0])

a,b="di","od"
c=f"{a}{b}"
print(f"hi {a=} hii {b!=}")
print(f"{a} leep {b}c {c} e")

a="python"
b="java  "
print(a)
print("Languaga %s is better tahn %s " %(a,b))
print("languagae {0} ia better than {1}".format(a,b))
print("a={0},b={1}".format(b,a))
print("{na
me} {another}".format(name=a,another=b))

foo="bar"
print(f"{foo             = }")
print(f"\t {foo}")

age=14_12_000
print(age)

import datetime
today=datetime.datetime.today()
print(today)
print(f"{today:%B  %d, %Y}")


str='''dileep'''
print(str)
str1='str'
print(str1)

tup2=(1,2)
x,y=tup2
print(x,y)

b=true
print(b)
print("\\\\\\di")
a='d'
b='g'
c=a+b
print(c,type(c),type(b))

print("name".isalnum())

p=3,4
print(p)
str1=str('str')
print(str)

k=['a','b','c']
 del k[1]
print(a)
m=k.pop()
print(m)


2="gae"
print(2)
print(2+3==4+4)
print(f"which is greater {2+3 != 3+4}",5+6)

d='dhoni'
e="dhoni"
f='''dhoni'''
g="""dhoni"""
print(d,e,f,g)
print(round(20.09))
str=123
print(str'str')

a=10
b=a-3
print(b)

str="dhoni"
print("my favis {1} and {0}".format(str,'raina'))

val=raw_input("enter a value :")
print(val)
val = input("Enter your value: ")
print(val)
name = input("Enter your name: ")
print("Hello " + name)


list=[0,1,2,3,4,5,6,7,8,9,3,4,5]
print(list)
list[2]='dhoni'
print(list)
list.remove(3)
print(list)
popped=list.pop(4)
print(f"popped element is {popped}")
print(list)
del list[6]
print(list)
list.append('dileep')
print(list)
list.insert(3,'sakshi')
print(list)
#list1=str(list)
#list.sort()
print(f"sorted list is : {list1}")
print(iter('a'))



a="dileep  is a      good boy"
list=list(a)
print(list)

squares=[]
for i in range(10):
    value=i**2
    squares.append(value)
print(squares)


s="fih"
s[1]='k'
print(s)

s1=[]
s=['1','dhoni','3','4','5',[3,4,5],6]

print(s[5)

s1=s.copy()
print(s1)
s[len(s):]=[6]
s.append([8])
print(s)



for i in s :
    s1.append(i)
print(s1)
s.pop()
print(s,s1)
print(f"{s[1].title()}")


s[2:4]='e'
print(s)

a,b,c,d,e=(1),('1'),[1],['1'],(1,)
print(type(a),type(b),type(c),type(d),type(e))

a=(1,2,3,4,5,6)
del a[2]
print(a)
a[len(a):]='f'
print(a)

b=('a','b','c','d')
c=(7,8,9,'e','f','g')

a=[1,2]
b=[3,4]
c=a.copy()
print(c)
c.pop()
print(a,c)

a={1,2,1,3}
print(a,type(a))
a.update('e')
#a[1]='e'
print(a)


num=[1,2,3,4,5,6,7]
#even=odd=[]
even=[]
odd=[]
for i in num :
    if( i%2 == 0 ):
        #print(f"the even numbers are : {i}")
        even.append(i)
    else :
        #print(f"{i} is odd")
        odd.append(i)
print(f"{even , odd}" ,sep="\n" )

a,b=1,2
if a<5 and b>0 :
    print("yayy")

a={'a':100 , 'b':200}
print(a['b'])

alien_0={"x_pos":0,"y_pos":2,"speed":'medium'}
print(f"current position  of alien_0 is :{alien_0['x_pos'],alien_0['y_pos']}")
if alien_0["speed"] == "medium" : alien_0["x_pos"]+=1 ;print(alien_0)

a,b,c=true,True,TRue
print(type(a,b,c))

def printing(name):
    print(f"my name is {name}")
printing('dileep')

print(type(2))


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"I am {self.name} and i am {self.age} old !!")

p1=person('dileep',27)
p2=person('dhoni',40)
print(p1.name)




details=[{'no':1111,'pin':111,'bal':30000},{'no':2222,'pin':222,'bal':30000},{'no':3333,'pin':333,'bal':30000}]

for detail in details :
    print("welcome to SBI-ATM !!!")


import sys
print(sys.path)
for module in sys.modules:
    print(module,sep="\n")
print(sys.modules)

from .Testing import pizza
pizza(8,'a','b','c')

import Testing
Testing.pizza(8,'a','b')

print('a'+'b')
a='c'
b='d'

print(a*5,b)
print(a,'bcd')

a='dileep'
a=a[0:2]+'m'+a[3:300] ; print(a)
a[2]='k'
print(a)




class dog:
    breed="animal"
    def __init__(self,name,age):
        self.n=name
        self.a=age

obj1=dog('jan',19)
print(obj1)
print(obj1.n,obj1.a)

a=11;print(type(a))
b=str(11) ; print(type(b)) ; c=int(b);print(type(c))
===9-========================================llllllllllllllllll


s="dileep"
print(s[::-1])

k=len(s)
for c in s :
    print(s[k-1],end="")
    k=k-1
print('\n')

k=list(s)
print(''.join(reversed(k)))

#fact(5)=5*4*3*2*1
sum=0
def factorial(x):
    while(x >= 2):
        print(f"computing fact of {x}")
        sum=sum+(x*factorial(x-1))
        print(sum)

factorial(5)


def fact(x):
    if(x==1) :
        return x
    else :
        return x * fact(x-1)
k=fact(5)
print(k)


from datetime import datetime
now=datetime.now();print(now)
print(now.strftime("%m-%y %H%S"))

import datetime
import time
while True:
    a=datetime.datetime.now()
    print(a.strftime("%H-%M-%S"))
    time.sleep(1)


import sys 
import time

for i in range(10):
    print(i)
    time.sleep(1)

print("d")
