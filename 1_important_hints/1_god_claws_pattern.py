#-------------------------------------------------------------------------------------------#
#                          content is learnt from                                           #
#https://www.youtube.com/watch?v=NCnPg_S_Eu8&list=PL4KX3oEgJcffJTxggH5LviQeMHiNagq3y&index=2#
#                                                                                           #
#-------------------------------------------------------------------------------------------#
#```````````````````import section````````````````#
import time 
#```````````````````end of import section`````````#

connection = True
paid = True
internet = True
online = False


def gods_claw_pattern():
    if not connection:
        print("no connection....")
        return
    
    if not paid:
        print("user had do the payment....")
        return

    if not internet:
        print("No internet....")
        return
    
    if not online:
        print("you are offline...")

named_tuple = time.localtime()
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)
gods_claw_pattern()
named_tuple = time.localtime()
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)