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
