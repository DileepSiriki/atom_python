'''
FUNCTIONS are 2 types :
    1. Normal using def keyword
    2. Anonymous using lambda keyword (functions that do not have a name)
In Python a function is defined using the def keyword
A parameter is the variable listed inside the parentheses in the function definition. parameter, It is a piece of information the function needs to do its job
An argument is the value that are sent to the function when it is called. So it is a is a piece of information that’s passed from a function call to a function
DOCSTRING  describes what the function does. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs
The docstrings can be accessed using the __doc__ method of the object or using the help function

Special Symbols Used for passing arguments:-
1.)*args (Non-Keyword Arguments)
2.)**kwargs (Keyword Arguments)

    def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

    # Driver code
    myFun(first ='Geeks', mid ='for', last='Geeks')


'''
def my_function():
  """ Basic function calling . This is called a DOCSTRING""" #-> DOCSTRING
  print("Hello from a function")
my_function()
print("USING THE DOC STRING :",my_function.__doc__)


'''
TYPES OF FUNCTION CALLS :
'''
#Positional Arguments -> order matters in positional arguments
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#Keyword Arguments -> order does not matter in keyword aruguments
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

#Default Parameter Value
#When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Optional values using default evaluates
def get_formatted_name(first_name, last_name, middle_name=''):
 """Return a full name, neatly formatted."""
 if middle_name:
     full_name = f"{first_name} {middle_name} {last_name}"
 else:
     full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Passing LISTS to functions
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Returning values
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
The asterisk in the parameter name *kids tells Python to make an empty tuple called kids and pack whatever values it receives into this tuple
'''

def my_function(*kids):
  print("The youngest child is",kids[2])
my_function("Emil", "Tobias", "Linus")

#Positional + Arbitary arguments
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
     print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
#Arbitary Keyword Arguments
#The double asterisks before the parameter **kid cause Python to create
an empty dictionary called kid and pack whatever name-value pairs
it receives into this dictionary
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing List as aruguments.
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#function definitions cannot be empty.
#if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error
def myfunction():
    pass

'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Use lambda functions when an anonymous function is required for a short period of time.
Lambda functions are used along with built-in functions like filter(), map() etc
SYNTAX :    lambda arguments : expression
'''
print(lambda a : a) #<function <lambda> at 0x000002999977CF70>

x = lambda a : a
print(x('dileep'))  #dileep

#A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

'''
The filter() function in Python takes in a function and a list as arguments. The function is called with all the items in the list .
A new list is returned which contains items for which the function evaluates to True
'''
my_list=[1,2,3,4,5,6,7]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)     #[2, 4, 6]

'''
The map() function in Python takes in a function and a list. The function is called with all the items in the list
A new list is returned which contains items returned by that function for each item.
'''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)     #[2, 10, 8, 12, 16, 22, 6, 24]

'''
A module is a file ending in .py that contains the code you want to import into your program .
When Python reads a .py file, the line "import xyz" tells Python to open the file xyz.py and copy all the functions from it into this program.
You don’t actually see code being copied between files because Python copies the code behind the scenes just before the program runs

create a module xyz.py with required functions and then :

import xyz -> all functions are available to use
xyz.function1() -> to use a function in xyz after importing

LOCAL SYMBOL TABLE & PRIVATE SYMBOL TABLE
import xyz -> available in private symbol table
from xyz import function_1 ->  to import only a specific function instead of all functions to save memory .
from xyz import function_0, function_1, function_2 -> to import more than one function
import xyz as a -> Aliasing a module name so that we can use it as a.function_1()
from xyz import function_1 as f1 -> Aliasing a function so that we can use it as xyz.f1()
from xyz import * -> import all functions  (now we can exclude .notation and use directly the function but not helpful for larger modules)
                  -> should not be used as some function names can be similar to module and the file we write .
                  -> As this pushes everything to local table and hence conflicts
There are two types of imports in Python: absolute and relative.
Absolute imports are where you import something on sys.path, like a built-in package.
Relative imports are where you import something that is relative to the program that you are writing.
Relative imports must be part of a package otherwise they cannot be run.
https://realpython.com/absolute-vs-relative-python-imports/
'''
#import this function as a module in testing.py
def pizza(size,*topplings):
    print(f"Thanks for the order for a {size}_inch pizza")
    for toppling in topplings:
        print(f"The topplings to add are : {toppling}")

pizza(16,'pepper','ginger','flakes')

'''
https://realpython.com/python-modules-packages/
Set env variable (SET PYTHONPATH=<path>) and restart atom .
When the interpreter executes the above import statement, it searches for <module>.py in a list of directories assembled from the following sources:
1. Put mod.py in the directory where the input script is located or the current directory, if interactive
2. Modify the PYTHONPATH environment variable to contain the directory where mod.py is located before starting the interpreter
    Or: Put mod.py in one of the directories already contained in the PYTHONPATH variable
3. Put mod.py in one of the installation-dependent directories, which you may or may not have write-access to, depending on the OS
    sys.path.append(r'C:\Users\user\Desktop\atom_python')
    Once you exit atom this will be deleted . so better add it in PATH variable for permanent effect
    control panel -> env variables -> new

The directory from which the input script was run or the current directory if the interpreter is being run interactively
The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
An installation-dependent list of directories configured at the time Python is installed
'''
import sys
print("PATHS SEARCHED FOR :")
for path in sys.path:
    print(f"--> {path}",sep="\n")
print("MODULES AVAILABLE :")
for module in sys.modules:
    print(f"--> {module}",sep="\n")

'''
PATHS SEARCHED FOR :
--> C:\Users\user\AppData\Local\Temp\atom_script_tempfiles
--> C:\Users\user\AppData\Local\Programs\Python\Python39\python39.zip
--> C:\Users\user\AppData\Local\Programs\Python\Python39\DLLs
--> C:\Users\user\AppData\Local\Programs\Python\Python39\lib
--> C:\Users\user\AppData\Local\Programs\Python\Python39
--> C:\Users\user\AppData\Local\Programs\Python\Python39\lib\site-packages

MODULES AVAILABLE :
--> sys
--> builtins
--> _frozen_importlib
--> _imp
--> _thread
--> _warnings
--> _weakref
--> _frozen_importlib_external
--> nt
--> _io
--> marshal
--> winreg
--> time
--> zipimport
--> _codecs
--> codecs
--> encodings.aliases
--> encodings
--> encodings.utf_8
--> encodings.cp1252
--> _signal
--> encodings.latin_1
--> _abc
--> abc
--> io
--> __main__
--> _stat
--> stat
--> _collections_abc
--> genericpath
--> ntpath
--> os.path
--> os
--> _sitebuiltins
--> site
'''
#OPTION $ -> store path of module in path variable
import sys
print(sys)  _#For user defined modules it prints  path of the module
sys.path.append(r'C:\Users\user\Desktop\atom_python')
print(sys.path)


'''
The dir() Function:
The built-in function dir() returns a list of defined names in a namespace.
Without arguments, it produces an alphabetically sorted list of names in the current local symbol table:

put the below code in Testing3.py if not available :
-------------------------------------------------------------
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]
def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
-------------------------------------------------------------

'''
print(dir())    #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
a,b,c='store',1,3
print(dir())    #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__','a', 'b', 'c']

#So use dir() to check what are all imported from an import statement .
#Execute LINE BY LINE
print(dir())
" ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__'] ""

qux = [1, 2, 3, 4, 5] ; print(dir())
"['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'qux'] ""

import Testing3 ; print(dir())
"['Testing3', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']"
print(Testing3.s)

from Testing3 import a, Foo ; print(dir()) ; print(a) ; x=Foo ; print(x)
'''
['Foo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a']
[100, 200, 300]
<class 'Testing3.Foo'> '''

from Testing3 import s as string ; print(dir()); print(string)
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'string']
If Comrade Napoleon says it, it must be right.  '''

from Testing3 import * ; print(dir())
''' ['Foo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'foo', 's'] '''



'''
EXECUTING MODULE AS A SCRIPT VS EXECUTING MODULE AS A MODULE :
Modules are often designed with the capability to run as a standalone script for purposes of testing the functionality that is contained within the module.
This is referred to as unit testing.  Done using condition ->> if (__name__ == '__main__'):

Put the below code in Testing3.py if not available ;
---------------------------------------------------------------------
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]
def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print(s)
print(a)
foo('quux')
x = Foo()
print(x)
-------------------------------------------------------------------------
OUTPUT :
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x000002179D5FFFD0>
-------------------------------------------------------------------------
When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.
Using this fact, you can discern which is the case at run-time and alter behavior accordingly

Now change the code to :
-----------------------------------------------------------------------
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]
def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
-----------------------------------------------------------------------
Now if you run it as a scrpit you get :
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x000001DF90E01FD0>

But if you use it as a module you will not get the unnecessary prints .
'''
#CODE IN TESTING3 WITHOUT if (__name__ == '__main__'):
import Testing3
print(Testing3.foo('Dhoni'))
'''
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<Testing3.Foo object at 0x0000020E74277D90>
arg = Dhoni
'''

#CODE IN TESTING3 with  if (__name__ == '__main__'):
import Testing3
print(Testing3.foo('Dhoni'))
'''
arg = Dhoni
'''


"""
PYTHON PACKAGES :
https://realpython.com/python-modules-packages/#python-packages
Suppose you have developed a very large application that includes many modules.
As the number of modules grows, it becomes difficult to keep track of them all if they are dumped into one location.
This is particularly so if they have similar names or functionality. You might wish for a means of grouping and organizing them.

Packages allow for a hierarchical structuring of the module namespace using dot notation.
In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names
"""
import sys
print(sys.path)
import atom_python.Testing3
print(atomm_python)
