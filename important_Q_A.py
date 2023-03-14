'''Here I write the Important Python Question and Answers'''
# # Shallow and DeepCopy in Python
# # ShallowCopy: A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# # Deep Copy: A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
#
'''
import copy
l = [[1,2], [3,4], [5,6], [7,8]]
# Shallow And Deep Copy
# ShallowCopy:
shallow = l.copy()
deep = copy.deepcopy(l)
print('Original list ',l)
print('Before Shallow Copy ',shallow)
print('Before Shallow Copy ',deep)

l[0][0] = 20
print('After list ',l)
print('After ShallowCopy ',shallow)
print('After DeepCopy ',deep)
'''

# # Create The Calender using Python

'''
import calendar
month = int(input('Enter Month'))
year = int(input('Enter Year'))

# print(calendar.month(year,month))
for month in range(1, 1 + month):
    print(calendar.month(year, month))
'''


# print the table using python

'''
number = int(input('Enter Number'))
value = int(input('Enter Value'))
for value in range(1,1+value):
    # print(number ,'*', value, '=', number*value)
    print(f'{number} * {value} = {number*value}')
'''

# What Is Name Space
# Ans. The Namespace is a naming system in python used to make sure name are unique to avoid the naming conflicts
'''
# Anagram Find Using Python:
from collections import Counter
def anagram(s,s1):
    return Counter(s) == Counter(s1)
    # or
    # return sorted(s) == sorted(s1)
    # or
    # return set(s) == set(s1)
print(anagram('evil','live'))
'''


# Given Input i want to print the price is gretherthen 100 that only print half values

input_details =  [{"name": "HDD","price": "$166" ,"brand": "Samsung", },
            {"name": "Monitor", "price": "$130","brand": "Dell",},
            {"name": "Mouse", "price": "$45","brand": "Logitech",}]

''' OP = [
    {'name': 'HDD', 'price': '83', 'brand': 'Samsung'}, 
    {'name': 'Monitor', 'price': '65', 'brand': 'Dell'},
    {'name': 'Mouse', 'price': '$45', 'brand': 'Logitech'}
]'''
'''
for i in input_details:
    if int(i['price'][1:])>100:
        i['price'] = str(int(i['price'][1:])//2)
print(input_details)
'''