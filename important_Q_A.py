# # Shallow and DeepCopy in Python
# # ShallowCopy: A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# # Deep Copy: A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
#
# import copy
# l = [[1,2], [3,4], [5,6], [7,8]]
# # Shallow And Deep Copy
# # ShallowCopy:
# shallow = l.copy()
# deep = copy.deepcopy(l)
# print('Original list ',l)
# print('Before Shallow Copy ',shallow)
# print('Before Shallow Copy ',deep)
#
# l[0][0] = 20
# print('After list ',l)
# print('After ShallowCopy ',shallow)
# print('After DeepCopy ',deep)


# # Create The Calender using Python

# import calendar
# month = int(input('Enter Month'))
# year = int(input('Enter Year'))
#
# # print(calendar.month(year,month))
# for month in range(1, 1 + month):
#     print(calendar.month(year, month))


# print the table using python

# number = int(input('Enter Number'))
# value = int(input('Enter Value'))
# for value in range(1,1+value):
#     # print(number ,'*', value, '=', number*value)
#     print(f'{number} * {value} = {number*value}')