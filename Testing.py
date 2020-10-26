import pyautogui
print(pyautogui.size())




k=10
j=9
print(k)
print("my age is ", k ,"and k is", k)
print("i am first %d and then %s" %(j,k))
a='dil'
b='eep'
print(a+b)
print(a*19)
print("how old are you"),
age=input()
k=input("how old are you?")
print(k)

name    = input("Enter Employee Name")
salary  = input("Enter salary")
company = input ("Enter Company name")
print("Printing Employee Details")

print ("Name", "Salary", "Company")
print (name, salary, company)



from sys import argv
script = argv
print("script is :",script)
print("firtdt variable is :",first)

str='dileep is a bad boy . {}'
str1='kumar'
k=90
print(str.format(k))


# Convert base-10 decimal integers
# to floating point numeric constants
print ("This site is {0:f}% securely {1}!!".
                    format(100, "encrypted"))

# To limit the precision
print ("My average of this {0} was {1:.2f}%"
            .format("semester", 78.234876))

# For no decimal places
print ("My average of this {0} was {1:.0f}%"
            .format("semester", 78.234876))

# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
        .format("binary", 100))

print("The {0} of 100 is {1:o}"
        .format("octal", 100))
