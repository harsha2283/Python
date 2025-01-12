
#RuntimeError 
# value = 0
# if value == 0:
#     print("error not started")
#     raise RuntimeError("The Value is true")
# else:
#     print("RuntimeError no executed")

#function with optional arguments 
def func_demo(parts = "any spare"):
    print("Deliver a car spare part ",parts)

#variable arguments 
'''Basically passing a raw data as a list'''
def func_var_argu(*args):
    for i in range(len(args)):
        print(f"args[{i}] -> {args[i]}")

#Variable keyword arguments 
'''passing data to the function in the format of a dictionary'''
def func_var_keyword_args(**dict_keys_values):

    for key, value in dict_keys_values.items():
        print(f"dict_keys_values - key - {key} -> dict_keys_values - value - {value}")


#main body 

result = 10 
#Expection handling
try:
    # result = 20/0
    result+"harsha"
except (ZeroDivisionError,TypeError):
    result = f"{result} {'harsha'}"
    print(result)


 #Dictionary 
my_dict = dict(name="harsha",gender=24,city="bengaluru")
for keys, values in my_dict.items():
   print(f"{keys} --> {values}")

print(my_dict.items())

print("using key collecting the data from the dictionary - ",my_dict["name"])

#extracting data from the Dictionary 
result = my_dict.get("age","default")
print(f"Exception handling instead of age we get gender -> {result}")



#list.extend(['harsha','vardhan'])

list_0 = ["first"]#[1,2,3,4,5]
list_1 = ["name","middle_name"]

list_2 = list_0 + list_1
print(list_2)

list_2.extend(["harsha", "vardhan"])
print(list_2)

#subset of list 
print("LIST SLICING")
print("-------------")
movie = ["Devara","ss","Kalki","SALAR","SS"]

print(movie[:2])
print(movie[-2:])
print(movie[2:3 ])



#with no arguments 
func_demo()

#with arguments 
func_demo("Door")

#variable arguments function call 
func_var_argu("piston","cylinder","gear oil","crank shaft") 

#variable keyword arguments 
func_var_keyword_args(name="Skoda",Type="car",Speed="120km/s",feul_type="Petrol")

