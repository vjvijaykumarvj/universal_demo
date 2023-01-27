# Here Iam Providing The Some Coding Questions And Answers

'''# Swaping Using Python'''
'''
a = int(input('Enter value'))
b = int(input('Enter value'))
print('Before Swaping A value',a)
print('Before Swaping B value',b)
print('**********************')
a,b = b,a
print('After Swaping A value',a)
print('After Swaping B value',b)
'''

'''
# Print the Prime Numbers
n1 = int(input('Enter Number'))
n2 = int(input('Enter Number'))
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
'''

'''
#  Print The Given Number Is Prime
n = int(input('Enter Number'))
for i in range(2,n):
    if n%i == 0:
        print(n,'Not Prime')
        break
else:
    print(n,'Prime Number')
'''
'''
# Print the Factorial Number
n = int(input('Enter Number'))
factotial = 1
if n>1:
    for i in range(1,1+n):
        factotial=factotial*i
print(factotial)

#################  or ###############
import math
print(math.factorial(5))
'''
'''
# Print The Polindrum Number
s = input('Enter Name')
if s == s[::-1]:
    print('Polindrum')
else:
    print('Not Polindrum')
'''
'''
# Seperete the integer,floating,string in list
l = ['vasu', 12, 12.4, 'vijay', 'sasi', 67, 900, 89.5, 'dasu']
numbers = []
names = []
floats = []
for i in l:
    if type(i) == int:
        numbers.append(i)
    if type(i) == str:
        names.append(i)
    if type(i) == float:
        floats.append(i)
print('Numbers ',numbers)
print('Names  ',names)
print('Decimal Numbers ',floats)
'''
'''
Q) What Is PEP8
A) the PEP Means Python Enhancement Proposal Its Has Set Of Recomandation About How to Write your Python Code More Rediable
Improve The Reusability And consistancy Of The Python Code
'''
'''
# Find Out The OWELS Using Lambda Function And Comprehension
n = ['vasu', 'hari', 'anu', 'umbrella', 'icecream', 'manasa']
s = list(filter(lambda x:x[0] in 'aeiou',n))
print(s)

s = [i for i in n if i[0] in 'aeiou']
print(s)
'''
'''
# find out the length of the charecter Position
n = ['vasu', 'hari', 'anu', 'umbrella', 'icecream', 'manasa', 'c++', 'Java', 'python']
m = list(filter(lambda x:len(x)>4 and x[0]=='i',n))
print(m)

s = [i for i in n if len(i)>4 and i[0]=='i']
print(s)
'''
'''
# Check the 2 Strings is Anagram
def Anagram(s,s1):
    return set(s) == set(s1)
print(Anagram('evil','live'))
'''
'''
# Split TheNumber of Words Given String
s = 'Hello WelcomeTo Python'
print(len(s.split()))
'''

'''
# find the Fabonicii Series
a,b = 0,1
n = int(input('Enter Number'))
for i in range(n):
    print(b)
    a,b = b,a+b
'''

'''
# Write The Programe set teh duplicate in list
l = [1,2,3,1,2,5,6,44,32,21,45,43,22,21,56,78,87,54,32]
m = list(set(i for i in l if l.count(i)>1))
print(m)
'''

'''
# What are the Inherit Styles In Django
They Are 3 Types In Django Inheritence Styles
1.Abstractbase Inheritance
2. Proxy model Inheritance
3. Multi Table inheritance

1. Abstractbase Inheritance:
To Hold the All the data information in parent Class You dont write the each child class
    
2. Proxy model Inheritance:
In This Style To Change The Python level behavior without changing the any model fields

3. Multi Table inheritance:
Its the subclassing of the existing models you need to change the each model in database table
'''
'''
# Print The Tables Using Python
number = int(input('Enter Numbers'))
value = int(input('Enter Values'))
for value in range(1,1+value):
    # print('{} * {} = {}'.format(number,value,number*value))
    print(number, '*', value, '=', number*value)
'''

'''
# What Is Admin.py And Manage.py In django
Admin.py is a command line utilty its used the administartion tasks
manage.py is a commanad line utility its deal for the django project
'''

'''
# What is Decorator in Python
#The decorator is a function its takes the another function as an arguments its extends the functionalty return fot the modified function with extends functionality

# for Exam using Decorator i will print the smaller case to all are upper cases

def ifinal(sum):
    def ifind(name):
        return sum(name).upper()
    return ifind
@ifinal
def sum(name):
    return name
print(sum('vijaykumar'))
'''
'''
# What Is Self In python
1. The Self Is teh refference variable 
2. its represent the current Objects
3. self is always inside the class
4. the self is not a keyword
5. self is the first Argument when we create the method and constructor
'''

'''
# What is Constructor In Python
1. The Constructor in python __init__(self)
2. Ones we create the objects the constructor will call automatically 
3. Each object created constructor called 
4. Constructor used to initialize the instance variable
5. construcor can be called like other methods
'''

'''
# What is Generator In python
1. the generator are simple create of iterators
2. generator is a like a function 
3. Which contains Yield keyword
4. by using __next__ also used

def find():
    for i in range(10):
        yield i
m = find()
for j in m:
    print(j)
'''

'''
# What Is Json
1. The Json Means Java Script Object Notation
2. Its free and Open-source
3. Using json Converting One place To anothe place
4. Its a Scalable
5. Compare to XML JSON Is Very Simple
6. Its Support The Both Front And BackEnd
7. No Depending The Other Libraries

Data Support In Json 
1. Number 2.Boolean 3.String 4.Object 5.Array 6.Null

JSON DoesNot Support Datatypes are
1. Function 2.Data 3.Undefined 4.Octal 5.Hexdecimal
'''

'''
# What Is Exception Handling In python
When We Write the python programee the syntax is correct bu its leads to some error The Error Does Not Stop 
so that we use the exception handlings
1.Try 2. Except 3.else 4.finally
1. Try Block used to to test the block of the code errors
2. except block used to handlng the errors
3. else block used to when there is no excetions it will be exceuted
4 finally block will be excecuted any time
'''

'''
# What Is Framework
1. Token: is a single element like as identifiers,keywords,operators,delimeters,litarals
2. statement: we make a code using tokens
3. Functio/class: The fgroup of the statement and reuseble code 
4. modules: Function/class kept in one file as a modules
5. pakages: The group of the modules kept in one foulder called pakages
6. library: The buindle of the pakages we call as library is bunch of the reusable code that may use in programme
7. Framework: Framework Simillar to the library which is provided the set of the reuseble code pakages
'''
'''
# Python Pakages
1.Numpy
2.Pandas
3.Matplotlib
4.SciKit-Learn
5.SciPy
6.TensorFlow
7.PyTorch
8.BeautifulSoup
9.Keras
10. Scrapy
'''

'''# How to get the current directory in python
import os
print(os.getcwd())
'''
'''
# What is Primary and Forenkey
PrimaryKey: The Primary key use to assure the Perticular column is unique
Forenkey: The Forenkey used to link between the 2 database table
'''

'''
# Print the Some Builtin Function In Python
1. all() 2. type() 3.any() 4.help() 5.dir() 6.min() 7.max() 8.sum() 9.len() 10.next() 11.hash() 12.bytes()
13. locals() 14.reversed 15 sorted() 16.map 17. range 18.property 19.zip 20.id()
'''

'''
# What is Format in python
1. The Format method format the specific value and insert the inside of placeholder
2. The placeholder like {} curlybrackes 
'''

'''
# What is .py and .pyc
1. The .py is a source code of python file
2. .pyc is a byte code of python file 
3. when the .pyc can be created when the code will be imported to some other sourse code the interpreter will takecare the .py to .pyc which helps the reduce the time
'''

'''
# what is CSRF
1. CSRF meand cross side request forgery
2. To avoid teh molicious attacks
3. Its generate teh token in server_side when the renderin the pages
4. The incomming request get not token its leads to error
5. Its Used to Security Perpose
'''

'''
# Using Python cll the Api
import requests
response = requests.get('http://127.0.0.1:8000/')
print(response.json())
'''

'''
What is Login_required
The Login required function used to to secure the views in the webapplication to forcing to the client to authenticated to validating user
'''

'''
What is enumerate function python
The enumerate function used to python convert a data objects to enumerate objects

x = ['sai', 'vamsi', 'das', 'hari', 'pallavi', 'sravani']
for i,j in enumerate(x,start=1):
    print(i,j)
'''
'''
# How can you generate the random Numbers in Python
### Python Random module is an in-built module of Python which is used to generate random numbers.
the random functions are 3 types
1.random:The random function return the floating point numbers between the (0,1)
2.randit: The randit function function return the integer numbers between the (x,y)
3.uniform:The random function return the floating point numbers between the (x,y)
'''

'''
# How can you findout the average number
# 1st way
l = range(10)
from statistics import mean
print((mean(l)))
# 2nd way
from functools import reduce
m = len(l)
s = reduce(lambda x,y:x+y,l)/m
print(s)
'''

'''
# Write the programe count the values
n = 'vijaykumar'
s = 0
m = []
for i in n:
    s = s+1
print(s)
'''

'''
# Sum the total vales
s = [1,2,3,4,5,6,7,8,9,10]
k = 0
for i in s:
    k = k+i
print(k)
'''

'''
# Print The Armstrong Number Using python
n = int(input('Enter Number'))
a = map(int,str(n))
b = map(lambda x:x**3,a)
if sum(b) == n:
    print(n,'Armstrong Number')
else:
    print(n,'Not Armstrong Number')
'''

'''
# Sorting The Given List
l = ['1', '0', '-2', '10', '8', '-9']
l.sort()
m = [int(i) for i in l]
print(m)
'''

'''
# Print The given list below 10 numbers
s = [19,67,9,4,3,8,-1.-34,-2,-7,12]
l = []
for i in s:
    if i>10:
        l.append(i)
print(l)
'''

'''
# Print the common letters using python
s = input('Enter name')
s1 = input('Enter name')
m = set(s) & set(s1)
for i in m:
    print(i)
'''

'''
# print the year calender
import calendar
month = int(input('Enter Month'))
year = int(input('Enter Year'))
for month in range(1,1+month):
    print(calendar.month(year,month))
'''

'''
# Count the number of elements repeated in string
m = 'Hellowelcomegoogle'
m = {i:m.count(i) for i in m}
print(m)
'''

'''
# find the dict sum values
d = {1:10, 2:20, 3:30, 4:40, 5:50}
sum = 0
for i in d.values():
    sum = sum+i
print(sum)
'''

'''
# print the list asending order to decending with out using sorting
l = [12,54,0,8,4,66,54,33,67,5,3,4,34,38]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
print(l)
'''
'''
# print the 3 highest numbers using python
l = [12,54,0,8,4,66,54,33,67,5,3,4,34,38]
l.sort()
N = 3
print(l[-N:])
'''