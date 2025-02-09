'''
File_name: 1_map.py
Topic_name: map function
Resource_used_to_learn: https://www.programiz.com/python-programming/methods/built-in/map
what can a user learn from this file:
1.how to use the map function
'''

plain_list = [1, 2, 3, 4, 5, 6]

#fucntion to add number 
def addition(number):
    return number+number

#syntax of the map function 
# map(function, iterables)

#Apply addition() to each item in the list plain_list
added_List = map(addition,plain_list)

#map function returns a map object this has to be converted to a list, tuple are any kind of datatype 
print(added_List)
map_list = list(added_List)

print(map_list)
help(map)