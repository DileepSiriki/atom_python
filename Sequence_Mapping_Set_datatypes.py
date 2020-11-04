#page 71
"""
Deals with :
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
"""

"""
LISTS :
Index Positions Start at 0, Not 1
A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family
In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas
Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired
By asking for the item at index -1, Python always returns the last item in the list
"""
subjects = ['python', "java", 'c++', 'GAWK']
print(subjects)     #['python', 'java', 'c++', 'GAWK'] -> converted to single quotes
languages = ["maths","english UK","science"]
print(languages)    #['maths', 'english UK', 'science']

print(languages[2])     #science
print(languages[1].capitalize())    #English uk
print(subjects[-1])     #GAWK -> This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth
print(languages[3])     #list index out of range

l=[1,2,3]
print(l[2.0])   #TypeError: list indices must be integers or slices, not float

languages = ["maths","english UK","science"]
print(f"my fav subject among all was {languages[1]}. ")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)           #['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'    #['ducati', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('karizma')
print(motorcycles)          #['ducati', 'yamaha', 'suzuki', 'karizma']
motorcycles.insert(1, 'pulsar') # To insert at a certain position
print(motorcycles)          #['ducati', 'pulsar', 'yamaha', 'suzuki', 'karizma']
del motorcycles[2]          #once del is used , you can not access the element again , so use pop() to access it .
print(motorcycles)          #['ducati', 'pulsar', 'suzuki', 'karizma']

list = [3, 5, 7, 8, 9, 20]
del list[0:3]
print(list)     #[9, 20]

#The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack
#Remember that each time you use pop(), the item you work with is no longer stored in the list.
#pop() is also permanent but the value can be caught to a variable.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)          #['honda', 'yamaha']
print(popped_motorcycle)    #suzuki
pop_centre=motorcycles.pop(1)   #pop(index) to pop element at an index
print(f"value popped is {pop_centre}") #value popped is yamaha

#If you do not know the index of the value then use the remove method to remove using the value name .
#The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed
languages = ["maths","english UK","science"]
languages.remove('science') #removing directly using value
print(languages)        #['maths', 'english UK']
difficult='maths'
languages.remove(difficult) #assigning to a variable and then removing using variable name
print(languages)        #['english UK']

#ORDERING A LIST
#sorting can be done only between elements os similar type . can not be done between int and string combination
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']
cars = ['audi', 'bmw', '9ab', 'subaru', 'toyota', '123', '23_ab' ]
cars.sort()
print(cars)     #['123', '23_ab', '9ab', 'audi', 'bmw', 'subaru', 'toyota']
print(cars[3])  #audi ->sort will change the order permanently
cars = ['audi', 'bmw','!ab','?cv','+er', '9ab', 'subaru', 'toyota', '123', '23_ab' ]
cars.sort()
print(cars)     #['!ab', '+er', '123', '23_ab', '9ab', '?cv', 'audi', 'bmw', 'subaru', 'toyota']

# sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
cars = ['audi', 'bmw','!ab','?cv','+er', '9ab', 'subaru', 'toyota', '123', '23_ab' ]
cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi', '?cv', '9ab', '23_ab', '123', '+er', '!ab']

#To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.
# can also accept a reverse=True parameter
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota'] -> affect is not permanent
print(cars)         #['bmw', 'audi', 'toyota', 'subaru']

#The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)     #['subaru', 'toyota', 'audi', 'bmw']
print(len(cars)) #4

a="dileep"
list=list(a)
print(list)     #['d', 'i', 'l', 'e', 'e', 'p']
a="dileep  is a      good boy"
list=list(a)
print(list)     #['d', 'i', 'l', 'e', 'e', 'p', ' ', ' ', 'i', 's', ' ', 'a', ' ', ' ', ' ', ' ', ' ', ' ', 'g', 'o', 'o', 'd', ' ', 'b', 'o', 'y']

s=[100,200,230,45]
print(min(s),max(s),sum(s))     #45 230 575

s=['1','2','3','4','5']
s[2:4]='e'
print(s)    #['1', '2', 'e', '5']
s=['1','2','3','4','5']
s[2:4]=[8,9]
print(s)    #['1', '2', 8, 9, '5']  # the values are iterated upon available count of evaluates.
s=['1','2','3','4','5','6','7']
s[2:5]=[8,9]
print(s)    #['1', '2', 8, 9, '6', '7'] #other fields will be deleted
s=['1','2','3','4','5','6','7']
s[2:2]=[8,9]
print(s)    #['1', '2', 8, 9, '3', '4', '5', '6', '7']
s+=['a','b']
print(s)    #['1', '2', 8, 9, '3', '4', '5', '6', '7', 'a', 'b']
s+=89
print(s)    #error because integers are not iterable . so you should provide [89] instead of 89

a=['a','b']
b=a.append(30)
print(b)    #None -> 30 gets appended but it will not reflect to b . we have to explicitly copy
print(a)
b=a
print(f"b is {b}")  #b is ['a', 'b', 30]

a=['3','5','8','1']
b=a.sort()
print(a,b)  #['1', '3', '5', '8'] None
a=['3','5','8','1']
b=sorted(a)
print(a,b) #['3', '5', '8', '1'] ['1', '3', '5', '8']

players=list(78)
print(players) #int object is not iterable
players=list('dhoni')
print(players)  #['d', 'h', 'o', 'n', 'i']

list=[0,1,2,3,4,5,6,7,8,9,3,4,5]    #list with duplicates
#Method-1 :
list1=[]
for i in list :
    if(i not in list1):
        list1.append(i)
print(f"List before {list} , list after {list1}")   #List before [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5] , list after [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Method-2 :
ints_list = [1, 2, 3, 4, 3, 2]
ints_list1 = list(set(ints_list))
print(ints_list1)  # [1, 2, 3, 4]

#Method-3 :
ints_list = [1, 2, 3, 4, 3, 2]
ints_list2 = list(dict.fromkeys(ints_list))
print(ints_list2)  # [1, 2, 3, 4]

#Method-4 :
ints_list = [1, 2, 3, 4, 3, 2]
for x in ints_list:
    if ints_list.count(x) > 1:
        ints_list.remove(x)
print(ints_list)  # [1, 2, 3, 4]

'''
SLICING
Always copy a list using slice . if we directly copy a duplicate is not created and just a refrence is created so an operation
on one set will do the same opration on another set .
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:])       #['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:-1])     #['charles', 'martina', 'michael', 'florence']
print(players[-3:])     #['michael', 'florence', 'eli']

set1=[1,2,3,4,5]
set2=set1
print(set1,set2)        #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
set1.append(6)
set2.append(7)
print(set1,set2)        #[1, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4, 5, 6, 7]

set1=[1,2,3,4,5]
set2=set1[:]            # COPYING USING SLICING
print(set1,set2)        #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
set1.append(6)
set2.append(7)
print(set1,set2)        #[1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 7]


'''
NAMING CONVENTION :
for cat in cats:
for dog in dogs:
for item in list_of_items:
'''
names=['dhoni','dileep','sakshi','chandu','aryana']
for name in names :
    print(name)
print(f"{name} is great !") #aryana is great

for value in range(1,5):
    print(value) # 1 2 3 4

for value in range(5):      #prints from 0 to value provided
    print(value) # 0 1 2 3 4

numbers = list(range(1, 6))
print(numbers)    #[1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))
print(even_numbers)  #[2, 4, 6, 8, 10]

squares=[value**2 for value in range(10)]
print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
