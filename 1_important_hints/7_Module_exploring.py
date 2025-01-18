'''
File name: 7_Module_exploring.py
'''

import time

print(dir(time))

print(help(time.perf_counter))

help(print)
#seperator it seperates the different values passed to the print function with the seperater mentioned the default seperator is a space character
print("Hi here i'm exploring","the print function",sep=" # ")

#end it holds a default values as "\n" but we can modify it to anything we need
print("Hi this is the magic string",end= '@')
print("see now this print statement is not printed in the new line")

with open("data_printed_by_print_function.txt","+a") as print_data_to_file :
    #file it will print the data in the file provided to it in the stdout (console)
    print("This data was printed in the file usign print functiona and a file attribute",file=print_data_to_file)

start = time.perf_counter_ns()
#flush parameter in print() function is used to immediately write the output to the console or file without buffering
print("This statement is printed using the flush parameter",flush=True)
stop = time.perf_counter_ns()
Delta_time = stop - start
print(f"time taken to print the flush=true print statement is {Delta_time}")

named_tuple = time.localtime()
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)
time.sleep(2)
named_tuple = time.localtime()
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)
