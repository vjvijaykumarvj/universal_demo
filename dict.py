""" Dict Important Q&A """
# Convert two lists into a dictionary
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d = {i:j for i,j in zip(keys,values)}
print(d)
########### or ##############
d = dict(zip(keys,values))
print(d)
'''

#  Merge two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d = {**dict1,**dict2}
print(d)
######## or ##########
x = dict1.copy()
x.update(dict2)
print(x)
'''

# Print the value of key ‘history’ from the below dict
'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['physics'])
'''

# Initialize dictionary with default values
'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
m = dict.fromkeys(employees,defaults)
print(m)
'''

# Create a dictionary by extracting the keys from a given dictionary
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d = {i:sample_dict[i] for i in keys}
print(d)
'''

# Delete a list of keys from a dictionary
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)
'''

# Check if a value exists in a dictionary
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(sample_dict['b'])
###### or ########
if 200 in sample_dict.values():
    print('yes')
else:
    print('No')
'''

# Rename key of a dictionary
'''
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['Country'] = sample_dict.pop('city')
print(sample_dict)
'''

# Get the key of a minimum value from the following dictionary
'''
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(sample_dict['Math'])
print(min(sample_dict))
'''

# Change value of a key in a nested dictionary
'''
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 10000
print(sample_dict)
'''