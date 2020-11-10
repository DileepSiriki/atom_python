'''
Python is an object oriented programming language.
In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes.
When you write a class, you define the general  behavior that a whole category of objects can have.

ATTRIBUTES :
Attributes are the variables that belong to class.
Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute

OBJECTS :
Almost everything in Python is an object, with its properties and methods.
Making an object from a class is called instantiation, and you work with instances of a class . It has the following
State : It is represented by attributes of an object. It also reflects the properties of an object.
Behavior : It is represented by methods of an object. It also reflects the response of an object with other objects.
Identity : It gives a unique name to an object and enables one object to interact with other objects.

SELF :
Class methods must have an extra first parameter in method definition. We do not give a value for this parameter when we call the method, Python provides it.
If we have a method which takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

NAMESPACE & SCOPE :
A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries,
The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits
The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function
A scope is a textual region of a Python program where a namespace is directly accessible

__init__ METHOD :
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state.
Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation.
It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

CLASS & INSTANCE VARIABLES :
Instance variables are for data unique to each instance and whose value is assigned inside a constructor or method with self
class variables are for attributes and methods shared by all instances of the class and are variables whose value is assigned in the class

CONSTRUCTORS :
Constructors are generally used for instantiating an object.
The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
In Python the __init__() method is called the constructor and is always called when an object is created.

        def __init__(self):     -> DEFAULT CONSTRUCTORS
        def __init__(self,x,y,z):   ->PARAMETERIZED CONSTRUCTOR

DESTRUCTORS :
Destructors are called when an object gets destroyed.
Not needed as much needed in C++ because Python has a garbage collector that handles memory management automatically.
The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted

class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

===========================
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()

'''
class MyClass:
    x = 5
print(MyClass) #<class '__main__.MyClass'>
print(type(MyClass)) #<class 'type'>

#Create an object of class MyClass
p1 = MyClass()
print(p1.x) #5

===========================
class Complex:
    name = "Complex Numbers "       ## class variable shared by all instances (remains same for all objects created)
    def __init__(self, realpart, imagpart):
         self.r = realpart          ## instance variable unique to each instance (varies on the arguments passed)
         self.i = imagpart          ## instance variable unique to each instance

x=Complex(3.0,-4.5)
print(x.name)
print(x.r,"And",x.i)

'''
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
The __init__() function is called automatically every time the class is being used to create a new object.
Objects can also contain methods. Methods in objects are functions that belong to the object.
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)   #John
print(p1.age)    #36
p1.age=45        #To change the value of an object .
print(p1.age)    #45
del p1.age       #To delete an attribute of an object
#print(p1.age)    #AttributeError: 'Person' object has no attribute 'age'
p1.myfunc()      #Hello my name is john
del p1           #Delete an object
#p1.myfunc()     # name 'p1' is not defined

'''
WRONG USE :
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']

CORRECT USE :
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

'''

'''
INHERITANCE :
'''
#PARENT class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#CHILD Class
class Student(Person):
  pass #when you do not want to add any other properties or methods to the class.
  def __init__(self, fname, lname):
    #add properties etc.
    #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    #Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    Person.__init__(self, fname, lname) #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    super().__init__(fname, lname) #make the child class inherit all the methods and properties from its parent

#TO inherit parents functionality + additional functionality
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridde
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
