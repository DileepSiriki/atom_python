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

s=['1','2','3','4','5']
s[2:4]='e'
print(s)
