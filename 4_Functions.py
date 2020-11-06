'''
In Python a function is defined using the def keyword
A parameter is the variable listed inside the parentheses in the function definition. parameter, It is a piece of information the function needs to do its job
An argument is the value that are sent to the function when it is called. So it is a is a piece of information that’s passed from a function call to a function
DOCSTRING  describes what the function does. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs
'''
def my_function():
  """ Basic function calling . This is called a DOCSTRING""" #-> DOCSTRING
  print("Hello from a function")
my_function()


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
lambda arguments : expression
'''
#A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

'''
A module is a file ending in .py that contains the code you want to import into your program .
When Python reads a .py file, the line "import xyz" tells Python to open the file xyz.py and copy all the functions from it into this program.
You don’t actually see code being copied between files because Python copies the code behind the scenes just before the program runs

create a module xyz.py with required functions and then :

import xyz -> all functions are available to use
xyz.function1() -> to use a function in xyz after importing
from xyz import function_1 ->  to import only a specific function instead of all functions to save memory .
from xyz import function_0, function_1, function_2 -> to import more than one function
import xyz as a -> Aliasing a module name so that we can use it as a.function_1()
from xyz import function_1 as f1 -> Aliasing a function so that we can use it as xyz.f1()
from xyz import * -> import all functions  (now we can exclude .notation and use directly the function but not helpful for larger modules)
                  -> should not be used as some function names can be similar to module and the file we write .

'''
