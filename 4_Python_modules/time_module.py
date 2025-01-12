import time

#1 asctime()
result = time.asctime()
print(result)

#2 strftime()
named_tuple = time.localtime()
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)