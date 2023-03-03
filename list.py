''' List Interview Coding Q&A'''
# what is List
'''
1. The list is data type in python 
2. List a mutable objects
3. Indexing slicing is support using list
4. Insertion order is preserved modification is done
5. List is not hashable.
6. List is represented using []
7. Homogeneous & Heterogeneous objects are allowed which means Lists need not be homogeneous always,
    a single list may contain data types like Integers, Strings, as well as Objects
8. List allows duplicate objects. 
'''


'''# Find the type and size of list
l = []
print(type(l))
print(l.__sizeof__())
'''

# 1.Reverse a list in Python
'''
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

###### or ########
list1 = [100, 200, 300, 400, 500]
l = list1[::-1]
print(l)

list1 = [100, 200, 300, 400, 500]
l = reversed(list1)
print(list(l))
'''

# Concatenate two lists index-wise
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
m = [i+j for i,j in zip(list1,list2)]
print(m)
'''

# Turn every item of a list into its square
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
m = [i**2 for i in numbers]
print(m)
#### or ######
for i in numbers:
    print(i**2)
###### or ######    
numbers = [1, 2, 3, 4, 5, 6, 7]
l = []
for i in numbers:
    l.append(i*i)
print(l)   
'''

# Concatenate two lists in the following order
'''
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
m = [i+j for i in list1 for j in list2]
print(m)
######## or ##########
for i in list1:
    for j in list2:
        print(i,j)
'''

# Iterate both lists simultaneously
'''
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[::-1]):
    print(i,j)
'''

# Remove empty strings from the list of strings
'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i:
        print(i)
############ or ##############

while '' in list1:
    list1.remove('')
print(list1)
############ or ##############
x = filter(None,list1)
print(list(x))
'''

# Add new item to list after a specified item
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
'''

# Extend nested list by adding the sublist
'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
'''

# Replace list’s item with new value if found
'''list1 = [5, 10, 15, 20, 25, 50, 20]
list1.remove(20)
list1.insert(3,100)
print(list1)
######### or ###########
l = list1.index(20)
list1[l] = 200
print(list1)

######## or ##########
list1[3] = 500
print(list1)
'''

# Remove all occurrences of a specific item from a list.
'''
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)
######## or #########
for i in list1:
    if i !=20:
        print(i)
'''
'''
l = [1,2,3,2,4,3]
def func(l):
    list = []
    for i in l:
        if i not in list:
            list.append(i)
    return (list)
x = func(l)
for j in x:
    print(j)
'''

# Chech the How Many time repeated in list of items
'''
l = [12, 1, 3, 4, 13, 54, 33, 67, 5, 4, 9, 3, 67]
m = {i for i in l if l.count(i)>1}
print(m)
'''

'''
#  How can you randomize the items of a list in place in Python?
import random
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
random.shuffle(x)
print(x)
'''
'''
import random
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
for i in x:
    random.shuffle(x)
print(x)
'''

# What IS Zip Function
# The Zip function is mapping the 2 or more sequences(list,tuple...etc) into a single iterable object.
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [12.2, 13.2, 14.2]
zipped = zip(list1,list2,list3)
print(list(zipped))
'''