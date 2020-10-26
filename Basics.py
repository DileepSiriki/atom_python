
#always open atom from cmd prompt -> windows+r -> cmd -> atom
#open the "Atom Package manager" from cmd line : type "apm"
#https://flight-manual.atom.io/ -> atom manual guide

#installing atom for first time , then do below to execute scripts.
#ctrl+shft+p -> type "view installed packages -> click install from left pane -> search for "SCRIPT" -> install SCRIPT "
#use "apm install ####" command to install packages from cmd prompt -> https://hackernoon.com/setting-up-atom-as-a-python-ide-a-how-to-guide-o6dd37ff
#Packages to install -> script , hydrogen , linter , linter-python (click on heading and do the below setting steps mentioned in chrome) , autocomplete python , atom file icons ,
#select a piece of code and then press ctrl+shft+b to run  the script.
#ctrl+, opens settings.
#GITHUB and GIT settings at https://www.hongkiat.com/blog/manage-git-github-atom/
#End of ATOM specifications .


#This is a single line comment .
'''
PYTHON PRACTICE
---------------
PY 2.X VS PY 3.X : https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
single line comments can be written using a '#'
Multiple line comments can be doen using """ comment """
Since Python will ignore string literals that are not assigned to a variable,
you can add a multiline string (triple quotes) in your code, and place your comment inside it
As long as the string is not assigned to a variable, Python will read the code, but then ignore it,and you have made a multiline comment.
Python is an object oriented programming language.
'''
#Below all statements are same . print can have "" or '' .
print("Dileep")
print ("Dileep")
print('Dileep')
#printf('Dileep') # printf is not defined in py3.x

# '' and "" are used to quote each other as shown below .
print("Dileep is 'gud'.") #Dileep is 'gud'.
print('Dileep is "gud".') #Dileep is "gud".

'''
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string
'''
a=1
b='name'
c="is JOHN"
print(a,b,c) #1 name is JOHN
#print(abc) #Error
#print(a+b+c) #unsupported operand type(s) for +: 'int' and 'str'
print(b+c) #nameis JOHN
#int and string can not be concatnated but we can first convert it into str and then concatnated.
print(str(a)+b+c) #1nameis JOHN

a = """This is a multi line string1
This is the principle behind
multiline comments ."""
print(a)

# "+" donot put a space while a "," puts a space between strings in print.
str1="string1"
str2="string2"
print(str1,str2) #string1 string2
print(str1+str2) #string1string2
print(str1+"is a string") #string1is a string
print(str1,"is a string") #string1 is a string
print("Strings are %s and %s" %(str1,str2)) #Strings are string1 and string2
print("Strings are %s and %s" %(str1,'dhoni')) #Strings are string1 and dhoni
#print(str2"Dileep") #Error as either + or , are absent .

#assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "Python is "
y = "awesome"
z =  x + y
print(z) #python is awesome

#\n is interpreted as a new line directly .
str4='first line\nsecond line'
print(str4)  #first line
             #second line

#GLOBAL Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#Python is awesome

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#Python is fantastic ->LOCAL
#Python is awesome ->GLOBAL

#WE CAN USE KEYWORD GLOBAL TO MAKE A VARIABLE GLOBAL IN A FUNCTION.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#PYthon is fantastic

#Also, use the global keyword if you want to change a global variable inside a function
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#PYthon is fantastic

"""
DATA TYPES :
Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
"""
#type() gives the variable data type
str3='2'
print(type(str3)) #<class 'str'>
str3=2
print(type(str3)) #<class 'int'>
str3=2.0
print(type(str3)) #<class 'float'>
str3 = ["apple", "banana", "cherry"]
print(type(str3)) #<class 'list'>

'''
x = ("apple", "banana", "cherry")            ->	tuple
x = range(6)                                 ->	range
x = {"name" : "John", "age" : 36}            ->	dict
x = {"apple", "banana", "cherry"}            ->	set
x = frozenset({"apple", "banana", "cherry"}) ->	frozenset
x = True                                     ->	bool
x = b"Hello"	                             -> bytes
x = bytearray(5)	                         -> bytearray
x = memoryview(bytes(5))	                 -> memoryview
'''

#to get a random number
import random
print(random.randrange(1,10))

#constructs an integer number from a string literal (providing the string represents a whole number)
z = int("3")
print(z,type(z)) #3 <class 'int'>
#z = int('abc') #error : abc is not a whole number for int conversion.

'''
STRING FUNCTIONS:
-----------------
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()   	Returns True if all characters in the string are lower case
isnumeric() 	Returns True if all characters in the string are numeric
isprintable()  	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()   	Returns True if the string follows the rules of a title
isupper()   	Returns True if all characters in the string are upper case
join()      	Joins the elements of an iterable to the end of the string
ljust()     	Returns a left justified version of the string
lower()     	Converts a string into lower case
lstrip()    	Returns a left trim version of the string
maketrans() 	Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()   	Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()    	Searches the string for a specified value and returns the last position of where it was found
rjust()     	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()    	Splits the string at the specified separator, and returns a list
rstrip()    	Returns a right trim version of the string
split() 	    Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
'''

a = b = "Hello, World!"
print(b[2:5]) #llo  ,Get the characters from position 2 to position 5 (not included):
print(b[-2]) # d
print(b[-5:-2]) #orl
print(len(b)) #13
print(b.strip()) # returns "Hello, World!" , removes any whitespace from the beginning or the end:
print(b.lower()) #hello, world!
print(b.upper()) #HELLO, WORLD!
print(a.replace("H", "J")) #Jello, World!
print(a.split(",")) # returns ['Hello', ' World!'] , splits the string into substrings if it finds instances of the separator
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #True
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) #False


#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
#Use the format() method to insert numbers into strings
quantity = 3
itemno = 567
price = 49.95
txt = "My name is John, and I am {}"
print(txt.format(quantity)) #My name is John, and I am 3
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567.

a='123'
b='dileep'
c='12abc'
print(a.isalpha()) #False
print(a.isdigit()) #True
print(c.isalnum()) #True
print(b.isalpha()) #True
print(b.isdigit()) #False

#can only be used with int defined as strings not as int. a='107' is valid a=107 is invalid for this functions .
a=107
#print(a.isalpha()) #AttributeError: 'int' object has no attribute 'isalpha'
b='reversed String'
print(reversed(b)) #<reversed object at 0x00C1A160> , outputs an object .Strings has no default reverse method .
print(list(reversed(b))) #['g', 'n', 'i', 'r', 't', 'S', ' ', 'd', 'e', 's', 'r', 'e', 'v', 'e', 'r'] , GIVES a list .
print(''.join(reversed(b))) #gnirtS desrever
print(b.find("v")) #2
print(b.index('v')) #2

#index returns a -1 on not finding a substring while find returns an error
print(b.find("z")) #-1
#print(b.index('z')) #ValueError: substring not found

b = "Hello, World!"
def rev():
    i=1
    while(i<=len(b)):
        print(b[-i],end="")
        i=i+1

print(b[0:len(b)]) #Hello, World!
print(b[::-1]) #!dlroW ,olleH
rev() #!dlroW ,olleH


'''
BOOLEANS
--------
Booleans represent one of two values: True or False.
You can evaluate any expression in Python, and get one of two answers, True or False
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
In fact, there are not many values that evaluates to False, except empty values,
such as (), [], {}, "", the number 0, and the value None.
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True
print(1 > 3) #false
print(bool(False)) #False
print(bool(None)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
x = 200
print(isinstance(x, int)) #True
print(isinstance(x, str)) #False

'''
FORMATTING :

s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
'''
# Convert base-10 decimal integers
# to floating point numeric constants
print ("This site is {0:f}% securely {1}!!".
                    format(100, "encrypted"))  #This site is 100.000000% securely encrypted!!

# To limit the precision
print ("My average of this {0} was {1:.2f}%"
            .format("semester", 78.234876)) #My average of this semester was 78.23%

# For no decimal places
print ("My average of this {0} was {1:.0f}%"
            .format("semester", 78.234876)) #My average of this semester was 78%

# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
        .format("binary", 100)) #The binary of 100 is 1100100

print("The {0} of 100 is {1:o}"
        .format("octal", 100)) #The octal of 100 is 144

'''
By default strings are left-justified within the field, and numbers are right-justified. We can modify this by placing an alignment code just following the colon.

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
'''

# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
                        .format("GeeksforGeeks", "geeks")) #GeeksforGeeks, is the computer science portal for geeks   !

# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
                        .format(40)) #It is    40 degrees outside!

# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
    .format("GeeksforGeeks", 2009)) # GeeksforGeeks was founded in             2009!


# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!"
        .format("GeeksforGeeks", 2009)) #GeeksforGeeks   was founded in 2009 !

print("{:*^20s}".format("Geeks")) #*******Geeks********

'''
TYPE CONVERSION :
'''
s = "10010"

# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)  #After converting to integer base 2 : 18

# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e) #After converting to float : 10010.0

# Python code to demonstrate Type conversion
# using  ord(), hex(), oct()

# initializing integer
s = '4'

# printing character converting to integer
c = ord(s)
print ("After converting character to integer : ",end="")
print (c) #After converting character to integer : 52

# printing integer converting to hexadecimal string
c = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (c) #After converting 56 to hexadecimal string : 0x38

# printing integer converting to octal string
c = oct(56)
print ("After converting 56 to octal string : ",end="")
print (c) #After converting 56 to octal string : 0o70

s = 'geeks'

# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c) #After converting string to tuple : ('g', 'e', 'e', 'k', 's')

# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c) #After converting string to set : {'k', 'g', 's', 'e'}

# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c) #After converting string to list : ['g', 'e', 'e', 'k', 's']

a = 1
b = 2

# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))

# printing integer converting to complex number
c = complex(1,2)
print ("After converting integer to complex number : ",end="")
print (c) #After converting integer to complex number : (1+2j)

# printing integer converting to string
c = str(a)
print ("After converting integer to string : ",end="")
print (c) #After converting integer to string : 1

# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (c) #After converting tuple to dictionary : {'a': 1, 'f': 2, 'g': 3}

#code for disabling the softspace feature
print('G','F','G', sep='') #GFG
print('09','12','2016', sep='-') #09-12-2016
print('pratik','geeksforgeeks', sep='@') #pratik@geeksforgeeks