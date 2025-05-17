'''
    Primitive Data Types : (Immutable, single value, less memory, copying creates new instances,
    limited methods and operations)
        1. Integer
        2. Float
        3. String
        4. Boolean
'''
import random

inttt = 23
floattt = 25.6


'''
    Non Primitive Data Types : (Mutable, multiple value, more memory(complex data), copying creates shallow or deep copies, rich set of methods and operations)
        1. List 
        2. Tuples
        3. Set
        4. Dictionary (hashmaps or associative array in other programming languages)
        5. String 
'''
# 1. List - 0 index based
courses  = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[0:2]) # value at index  2 is not included
print(courses[:2]) # array slicing
print(courses[2:])
# courses.append('Art')
print(courses)
courses.insert(0,['Art','Education'])
courses.extend(0, ['Art', 'Education'])
popped = courses.pop()
courses.reverse()
courses.sort(reverse=True)
for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)
courses_1 = sorted(courses) # creates a new sorted version instead of modifying the original array
print('Art' in courses)
print(courses.index('Art'))
list1 = [100,22,3,40]
print(min(list1))
print(max(list1))
print(sum(list1))
list1.append(5)
print(list1)
list2 = ["hello", 345, [12,23]]
print(list2[2][0])
list1.sort()
print('30',list1)

course_str = ', '.join(courses)
print(course_str)
new_list = course_str.split(', ')
print(new_list)

# 2. Tuples - Immutable objects
tuple_1 = ('History', 'Art', 'Math')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
tuple_1[0] = 'Art' # throws error as tuple are immutable

# 3. Sets - unordered and no duplicates
cs_courses  = {'History', 'Maths', 'Physics'}
print(cs_courses) # prints in random order
print('Maths' in cs_courses)

art_courses = {'History', 'Maths', 'Art', 'Design'}
# intersection

print(cs_courses.intersection(art_courses))
# differences

print(cs_courses.difference(art_courses))

# Union

print(cs_courses.union(art_courses))

# 4 Dictionaries and Operations : (Key Value data structure)
# Key can be any immutable object

student = {'name':'John', 'age': 25, 'courses' : ['Maths', 'CompSci']}
print(student)
print(student['name'])
print(student.get('name'))
print(student.get('phone', "not found")) # def value
student['phone'] = '345-34567-234567'
student['name'] ='Jane'
print(student)
student.update({'name':'Janani', 'age':28, 'city':'Chennai'})
Age = student.pop('age')
# del student['age'] # pop already removes age
for key, value in student.items():
    print(key, value)

print(len(student)) # returns the count of key in the dict
print(student.keys())
print(student.values())
print(student.items())


# Empty Lists
empty_list = []
empty_list = list()


# Empty Tuples
empty_list = ()
empty_list = tuple()

# Empty Sets
empty_list = {} # This is wrong. THis is actually a Dictionary
empty_list = set()


# Exercises to learn basic datatypes

# 1. Reverse the list
A1 = [1,2,3,4,5]
A1.append(6)
A1.reverse()
print('39', A1)
print('40',A1[::-1])
# Using Acc
acc = []
for elem in A1:
    acc.append(elem)

print('46', acc)

# 2. Perform union of two sets

Set1 = set(range(1,51))
Set2 = set(range(51,101))
Set3 = Set1.union(Set2)
Set4 = Set1|Set2 # Use 'Pipe' Symbol for union
# print('53', Set3)
# print('54', Set4)


# 3. Unpack the tuple into variables
A2 = (1,"janani", 28)
Id, Name, Age = A2
print(f'The Id : {Id} Name : {Name} Age : {Age}')

# 4. Update the value of an existing key
print('62',A1)
A1[0] = 100
print('64',A1)
print('66', A2)
# A2[2] = 29 # generates an error as tuples are immutable
print('68', A2)

# 5. Count the occurrences of an element



# 6. Check if two sets are disjoint
# 7. Slice the tuple from index 2 to 4
# 8. Iterate over dictionary keys and values
# 9. Insert an element at index 2
# 10. Create a set with 5 elements
# 11. Convert a list to a tuple
# 12. Delete a key-value pair
# 13. Reverse the list
# 14. Check if a set is a subset of another
# 15. Check if a value exists in the tuple
# 16. Delete a key-value pair
# 17. Slice the list from index 1 to 4
# 18. Convert a list to a set
# 19. Access an element by index
# 20. Get all keys from the dictionary
# 21. Count the occurrences of an element
# 22. Convert a list to a set
# 23. Access an element by index
# 24. Iterate over dictionary keys and values
# 25. Insert an element at index 2
# 26. Check if two sets are disjoint
# 27. Count the occurrences of a value
# 28. Use dictionary comprehension
# 29. Reverse the list
# 30. Convert a list to a set
# 31. Slice the tuple from index 2 to 4
# 32. Add a new key-value pair
# 33. Insert an element at index 2
# 34. Find the length of a set
# 35. Access an element by index
# 36. Iterate over dictionary keys and values
# 37. Slice the list from index 1 to 4
# 38. Create a set with 5 elements
# 39. Slice the tuple from index 2 to 4
# 40. Merge two dictionaries
# 41. Insert an element at index 2
# 42. Add an element to the set
# 43. Count the occurrences of a value
# 44. Merge two dictionaries
# 45. Remove an element from the list
# 46. Convert a list to a set
# 47. Unpack the tuple into variables
# 48. Get all values from the dictionary
# 49. Sort the list in ascending order
# 50. Add an element to the set
# 51. Find the index of a value
# 52. Check if a key exists in the dictionary
# 53. Reverse the list
# 54. Perform union of two sets
# 55. Nest a tuple inside another tuple
# 56. Iterate over dictionary keys and values
# 57. Append an element to the list
# 58. Create a set with 5 elements
# 59. Slice the tuple from index 2 to 4
# 60. Add a new key-value pair
# 61. Append an element to the list
# 62. Perform union of two sets
# 63. Access an element by index
# 64. Get all keys from the dictionary
# 65. Sort the list in ascending order
# 66. Create a set with 5 elements
# 67. Check if a value exists in the tuple
# 68. Get all values from the dictionary
# 69. Insert an element at index 2
# 70. Perform intersection of two sets
# 71. Count the occurrences of a value
# 72. Get all keys from the dictionary
# 73. Slice the list from index 1 to 4
# 74. Perform intersection of two sets
# 75. Convert a list to a tuple
# 76. Use dictionary comprehension
# 77. Count the occurrences of an element
# 78. Check if two sets are disjoint
# 79. Slice the tuple from index 2 to 4
# 80. Iterate over dictionary keys and values
# 81. Append an element to the list
# 82. Perform intersection of two sets
# 83. Find the index of a value
# 84. Check if a key exists in the dictionary
# 85. Remove an element from the list
# 86. Find the length of a set
# 87. Convert a tuple to a list
# 88. Get all keys from the dictionary
# 89. Find the index of a specific element
# 90. Check if two sets are disjoint
# 91. Convert a tuple to a list
# 92. Get all keys from the dictionary
# 93. Create a list of 5 integers
# 94. Perform intersection of two sets
# 95. Convert a list to a tuple
# 96. Check if a key exists in the dictionary
# 97. Insert an element at index 2
# 98. Perform difference of two sets
# 99. Convert a tuple to a list
# 100. Get all keys from the dictionary
