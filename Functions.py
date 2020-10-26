'''
In Python a function is defined using the def keyword
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that are sent to the function when it is called.
'''
def my_function():
  print("Hello from a function")

my_function()

'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
#Keyword Arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Arbitary Keyword Arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

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
