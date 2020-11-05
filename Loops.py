'''
IF statement:
'''

a,b=1,2
if a<5 and b>0 : print("yayy") # -> && should not be used anymore .
if a==1 or b==1 : print("super") # -> || should not be used anymore
if a in range(5) : print("cool")
if b not in range(2) : print("not so cool")



'''
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
The else keyword catches anything which isn't caught by the preceding conditions.
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
the else block can be omitted and is not mandatory
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") #if only one statement in if loop

#Pass statement
a = 33
b = 200
if b > a:
  pass

 '''
With the break statement we can stop the loop even if the while condition is true:
With the continue statement we can stop the current iteration, and continue with the next:
break leaves a loop, continue jumps to the next iteration.
Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
 '''
#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#range
for x in range(2,6):
    print(x) #2,3,4,5
for x in range(6):
    print(x) #0,1,2,3,4,5
