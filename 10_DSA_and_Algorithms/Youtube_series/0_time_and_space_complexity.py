#Time Complexity 
import time

def loop_through_list(data):
    local_var = 0
    for i in data:
        print(f"element in index[{0}] -> {1}".format(local_var,i))


my_list = list(range(10))
start_time = time.time()
#Start your coding from here
loop_through_list(my_list)
stop_time = time.time()

print(f"The time taken to execute the function is {0}".format((stop_time-start_time)))
