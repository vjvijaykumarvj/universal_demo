''' String Important Q&A '''

# Create a string made of the first, middle and last character
'''
str1 = "James"
print(str1[::2])
print(str1[0:5:2])
'''

# Arrange string characters such that lowercase letters should come first
'''
str1 = 'PyNaTive'
u = []
l = []
for i in str1:
    if i.isupper():
        u.append(i)
    if i.islower():
        l.append(i)
print(''.join(l+u))
'''

# Count all letters, digits, and special symbols from a given string
'''
str1 = "P@#yn26at^&i5ve"
n = 0
d = 0
s = 0
for i in str1:
    if i.isalpha():
        n = n+1
    elif i.isdigit():
        d = d+1
    else:
        s = s+1
print('numbers',n)
print('names',d)
print('extra',s)
'''

# Find all occurrences of a substring in a given string by ignoring the case
'''
str1 = "Welcome to USA. usa awesome, isn't it?"
x = str1.lower()
print(x.count('usa'))
'''

# Calculate the sum and average of the digits present in a string
'''
str1 = "PYnative29@#8496"
count = 0
total = 0
for i in str1:
    if i.isdigit():
        count = count+1
        total = total+int(i)
print(total)
print(count)
print(total/count)
'''

# Write a program to count occurrences of all characters within a string
'''
str1 = "Apple"
d = {i:str1.count(i) for i in str1}
print(d)
'''

# Reverse a given string
'''
str1 = "PYnative"
s = ''.join(reversed(str1))
print(s)
###### or ########
print(str1[::-1])
'''

# Split a string on hyphens
'''
str1 = 'Emma-is-a-data-scientist'
for i in str1.split('-'):
    print(i)
'''


# Replace each special symbol with # in the following string
'''
import string
str1 = '/*Jon is @developer & musician!!'
m = '#'
for i in string.punctuation:
    str1  = str1.replace(i,m)
print(str1)
'''