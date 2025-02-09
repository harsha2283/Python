'''
File_name: 1_closure.py
Topic_name: closure
Resource_used_to_learn:
1.https://www.programiz.com/python-programming/closure
2.https://www.youtube.com/watch?v=8Lu5DdTxGCU&list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc&index=12
what can a user learn from this file:
1.closure : closure is a nested function that helps us access the outer function's variables even after the outer function is closed
'''

def outer_function():
    num=0
    def inner_function():
        nonlocal num
        num +=1
        return num
    return inner_function

#call the outer_function()
out1 = outer_function()
out2 = outer_function()

#calling the inner_function()
print(out1())
print(out1())
print(out1())

#calling the outer_function()
print(out2())
 