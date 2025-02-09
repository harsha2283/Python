'''
File_name: 02_mutiple_args.py
Topic_name: *args and **kwargs
Resource_used_to_learn: https://www.programiz.com/python-programming/args-and-kwargs
what can a user learn from this file:
1.usage of the *args(No keyward arguments) and **kwargs(keyword arguments) these are used when we unsure about the number of the arguments to pass to the function
'''

#non-keyword arguments 
def non_keyword_agruments_func(*input_args):
    count = 0

    for u in input_args:
        count += u
    
    print(f"Total sum of *args = {count}\nTotal number of arguments passed = {len(input_args)}")

#keyword arguments
def keyword_arguments_function(**input_kwargs):
    print(f"number of Kwargs passed - {len(input_kwargs)}")
    for key,value in input_kwargs.items():
        print("{} is {}".format(key,value))


data:list = [1,2,3,4,5,6]
dict_data:dict = {"key":"value", "sun":"moon", "day":"night", "black":"white"}
#passing multiple args 
non_keyword_agruments_func(1,2,3,4,5)

#passing a list as a variable argument
non_keyword_agruments_func(*data)

#passing multiple arguments
keyword_arguments_function(name = "Harsa",age = 25, surname = "Kothinti")

#passing a dictionary  
keyword_arguments_function(**dict_data)


