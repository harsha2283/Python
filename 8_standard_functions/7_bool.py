'''
File_name: 7_bool.py
Topic_name: bool function
Resource_used_to_learn: 
what can a user learn from this file:
1.how to use the bool function
'''

list = [0, 2, 3.4, "string", 0b0011, 0b0000, None, False, [] ]

#checking for which values the Bool will give True or False values
for element in list:
    print(f"bool({element}) returned - {bool(element)}")

help(bool)