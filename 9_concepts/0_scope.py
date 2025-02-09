'''
File_name: 0_scope.py
Topic_name: scope
Resource_used_to_learn: https://www.youtube.com/watch?v=e_UgAqOdEXY&list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc&index=11
what can a user learn from this file:
1.scope of the variables
'''

# global variable
amount = 100

def scope_function(request):
    #global with in the function
    func_scope = 200

    #using the global keyword to modify the global variable
    global amount
    amount = amount - request
    print(f"amount after deducting the requested amount {amount} - from scope_function()")
    def local_fun():
        #modifying the function global variable using nonlocal keywaord
        nonlocal func_scope
        func_scope += 100
        print(f"func_scope var value = {func_scope} - from the local_func()")

    print(f"func_scope var - {func_scope} <- before calling the local_func()")
    local_fun()
    print(f"func_scope var - {func_scope} <- after calling the local_func()")

print("set1")
scope_function(request=10)
print("set2")
#Every time we call the scope_function the func_scope local global variable will be redefined to be used again
scope_function(request=10)

print(f"amount after deducting the requested amount {amount} - after calling scope_function()")