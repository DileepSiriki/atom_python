'''
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
print(thislist)

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
