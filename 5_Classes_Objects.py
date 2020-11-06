'''
Python is an object oriented programming language.
In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes.
When you write a class, you define the general  behavior that a whole category of objects can have.
Almost everything in Python is an object, with its properties and methods.
Making an object from a class is called instantiation, and you work with instances of a class
'''
class MyClass:
    x = 5
print(MyClass) #<class '__main__.MyClass'>
print(type(MyClass)) #<class 'type'>

#Create an object of class MyClass
p1 = MyClass()
print(p1.x) #5

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
