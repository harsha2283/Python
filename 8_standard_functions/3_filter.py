'''
File_name: 3_filter.py
Topic_name: filter function
Resource_used_to_learn: https://www.programiz.com/python-programming/methods/built-in/filter
what can a user learn from this file:
1.how to use the filter function
'''

#function
def longer_than_4(string):
    return len(string) > 4

strings = ["Hi", "Harsha", "Vardhan", "Reddy", "filter"]

#filter function
# filter(function, iterables)
strings_longer_than_4 = filter(longer_than_4, strings)

print(strings_longer_than_4)

list_of_strings_ge_4 = list(strings_longer_than_4)
print(list_of_strings_ge_4)