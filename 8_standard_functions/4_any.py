'''
File_name: 4_any.py
Topic_name: any function
Resource_used_to_learn: https://www.programiz.com/python-programming/methods/built-in/any
what can a user learn from this file:
1. how to use the any function
'''

any_list = [0,True, 5,"string"]
False_list = [0, False]
#any returns False since the list doesn't have any element in it 
print(f"if none of the elements from the list return false for the following experssion boolean(data) - {any(False_list)} \n")

#if anyone of the element in the list is true any() returns True
print(f"if any one of the elements on the list yeilds boolen(data) = true than the any() returns true {any(any_list)} \n")

help(any)