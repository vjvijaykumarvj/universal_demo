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

