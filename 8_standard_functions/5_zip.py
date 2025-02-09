'''
File_name: 5_zip.py
Topic_name: zip function
Resource_used_to_learn: https://www.programiz.com/python-programming/methods/built-in/zip
what can a user learn from this file:
1.how to use the zip function
'''

numbers = [1, 2, 3, 4, 5]
strings = ['one', 'two', 'three', 'four', 'five']

#no iterables are passed to the functions 
result = zip()

#converting iterator to list
result_list = list(result)

#printing the list which is created with no agruments passed the zip function
print(f"zipping  - \n  Zip() - function with no iterables passed - {result_list}")

#Iterables passed to the zip function yeilds a tuple 
zipped_tuple = zip(numbers, strings)

#converting the tuple into a list
zipped_list = list(zipped_tuple)

#printing the zipped list
print(f"\nzipping  - \n  zip(iter1, iter2) - function with 2 iterables passed - {zipped_list} ")

# unzipping the zipped data 
numbers_unzip, strings_unzip = zip(*zipped_list)

print(f"\nUnzipping - \n  iter1, iter2 = zip(*zipped_data_list)  - \n iter1 - {numbers_unzip} \n iter2 - {strings_unzip}")

help(zip)
