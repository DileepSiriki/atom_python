'''
Deals with :
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset

-> List is a collection which is ordered and changeable. Allows duplicate members.
-> Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
-> Set is a collection which is unordered and unindexed. No duplicate members.
-> Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
-> Lists and tuples are ordered and can contain duplicates .
-> Sets are unordered and cannot contain duplicates. you cannot be sure in which order the items will appear.

'''

'''
LISTS:
------
A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
First item has index 0 and the last one has index -1.
A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family
In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas
Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired
By asking for the item at index -1, Python always returns the last item in the list
'''
thislist = ["zaw", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist) #['zaw', 'apple', 'banana', 'cherry']
print(thislist[1]) #apple
print(thislist[-1]) #mango
print(thislist[2:5]) #['banana', 'cherry', 'orange']
print(thislist[::-1]) #['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple', 'zaw']
print(reversed(thislist)) #<list_reverseiterator object at 0x01F3A148>
print(list(reversed(thislist))) #['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple', 'zaw']
print(''.join(reversed(thislist))) #mangomelonkiwiorangecherrybananaapplezaw
print(','.join(reversed(thislist))) #mango,melon,kiwi,orange,cherry,banana,apple,zaw
thislist[1] = "blackcurrant" #to change the list
print(thislist) #['zaw', 'blackcurrant', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
for x in thislist: #loop the list
  print(x) #Prints one entry per line
for x in thislist:
  print(x,end=",") #zaw,blackcurrant,banana,cherry,orange,kiwi,melon,mango,
if "apple" not in thislist:
    print("YOO !!!") #YOO !!!
print(len(thislist)) #8
thislist.append("orange")
print(thislist) #['zaw', 'blackcurrant', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange']
thislist=['zaw', 'blackcurrant', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345, 56]
print(len(thislist)) #11
thislist.insert(1, "coconut")
print(thislist) #['zaw', 'coconut', 'blackcurrant', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345, 56]
thislist.remove("banana")
print(thislist) #['zaw', 'coconut', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345, 56]
#pop() method removes the specified index, (or the last item if index is not specified):
print(thislist.pop()) #56
print(thislist) #['zaw', 'coconut', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345]
print(thislist.pop(3)) #cherry
print(thislist) #['zaw', 'coconut', 'blackcurrant', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345]
print(thislist.append("Dhoni")) #None
del thislist[0]
print(thislist) #['coconut', 'blackcurrant', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345, 'Dhoni']
del thislist #deletes the list completely
print(thislist) #name 'thislist' is not defined
thislist=['coconut', 'blackcurrant', 'orange', 'kiwi', 'melon', 'mango', 'orange', 345, 'Dhoni']
thislist.clear() #empties the list
print(thislist) #[]
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #copy a list to another list. list1=list2 would not work. Similar to mylist = list(thislist) .
print(mylist) #["apple", "banana", "cherry"]
mylist = list(thislist) #similar to copy

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]

for x in list2:
  list1.append(x)
print(list1) #['a', 'b', 'c', 1, 2, 3]

list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3, 1, 2, 3]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) #['apple', 'banana', 'cherry']


subjects = ['python', "java", 'c++', 'GAWK']
print(subjects)     #['python', 'java', 'c++', 'GAWK'] -> converted to single quotes
languages = ["maths","english UK","science"]
print(languages)    #['maths', 'english UK', 'science']

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

players=list(78)
print(players) #int object is not iterable
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



'''
TUPLES :
--------
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
Accessing tuples is similar to accessing that of lists.
To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
We can not add or remove items directly from a tuple
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')
#Changing tuples is not possible. So convert them to lists and then change the value and then change the list to tuple again.
y = list(thistuple)
y[1] = "kiwi"
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')
del thistuple[1]
del thistuple #deletes the complete touple
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2 #Add tuples
print(tuple3) #('a', 'b', 'c', 1, 2, 3)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #3
x = thistuple.find(8) #'tuple' object has no attribute 'find'

'''
SETS :
------
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
Sets are a mutable collection of distinct (unique) immutable values that are unordered.
you cannot be sure in which order the items will appear.
You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
Once a set is created, you cannot change its items, but you can add new items.

add()	                Adds an element to the set
clear()	              	Removes all the elements from the set
copy	              	Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update()	    Removes the items in this set that are also included in another, specified set
discard()	            Remove the specified item
intersection()	        Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	            Returns whether another set contains this set or not
issuperset()	        Returns whether this set contains another set or not
pop()	                Removes an element from the set
remove()	            Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
union()	                Return a set containing the union of sets
update()	            Update the set with the union of this set and others
symmetric_difference_update()	inserts the symmetric differences from this set and another

'''
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'cherry', 'apple', 'banana'}
print("banana" in thisset) #True
thisset.add("orange") #to add one item
thisset.update(["orange", "mango", "grapes"]) #to add more than one item
print(thisset) #{'apple', 'mango', 'orange', 'banana', 'grapes', 'cherry'}
thisset.remove("banana") #If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana") #If the item to remove does not exist, remove() will NOT raise an error.
print(thisset) #{'orange', 'cherry', 'mango', 'apple', 'grapes'}
x = thisset.pop() #Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
print(x) #orange
print(thisset) #{'apple', 'cherry', 'mango', 'grapes'}
thisset.clear()
del thisset

#Both union() and update() will exclude any duplicate items
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{1, 2, 3, 'b', 'a', 'c'}
set1.update(set2)
print(set1) #{1, 2, 3, 'c', 'b', 'a'}
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'apple', 'banana', 'cherry'}

a={3,4,1,2}
print(type(a)) #<class 'set'>
print(sorted(a, reverse=True)) #[4, 3, 2, 1]
print(sorted(a)) #[1, 2, 3, 4]
print(type(sorted(a))) #<class 'list'>
print(type(a)) #<class 'set'>

'''
DICTIONARIES :
--------------
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict)) #3
#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"] ; print(x)
x = thisdict.get("model") ; print(x)
thisdict["year"] = 2018 ; print(thisdict.get("year")) #changing dict items
thisdict["color"] = "red" ; print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'} , to add items
thisdict.pop("model") #remove items
thisdict.popitem() #removes the last inserted item (in versions before 3.7, a random item is removed instead)
del thisdict["year"] #remove specific item
thisdict.clear() #empties the dictionary
del thisdict #delete dict completely

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #copy a dict
print(mydict)
for x in thisdict.keys():
  print(x)   #prints only keys , one per each line
for x in thisdict.values():
  print(x) #prints only values, one per each line
for x, y in thisdict.items():
  print(x, y) #prints both keys and values , one per each line
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


#NESTED DICTIONARIES:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
