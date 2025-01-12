#Source of the knowledge:
# https://www.youtube.com/watch?v=AppKIaME5_I


import json

my_dict = {"sons":[{"name":"Harsha","age":25,"DOB":"02/02/2000"},{"name":"Narayana","age":28,"DOB":"07/03/1997"}]}


#Collecting the data from the ditionary and writeing it into a JSON file
json_str = json.dumps(my_dict, indent=4)

with open(f"D:\\My_docs\\python\\learning\\4_Python_modules\\Json_module\\sons.json","w") as f:
    f.write(json_str)

#Collecting the data from the JSON file and reading it into a dictionary
with open("D:\\My_docs\\python\\learning\\4_Python_modules\\Json_module\\sons.json","r") as f:
    json_object = json.loads(f.read())

print(json_object)
print(json_object["sons"][1]["name"])
