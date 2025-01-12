'''
what is the constructor?
know more in the below website
https://www.programiz.com/article/python-self-why
'''
class Constructor:
    def __new__(cls, *args, **kwargs):
        print("From the __new__ Dundr method")
        print(cls)
        print(args)
        print(kwargs)

        #Create the object and return it 
        creating_base_object = super().__new__(cls)
        return creating_base_object
    
    def __init__(self, name="Name is missing", age=1):
        print("From the init function")
        self.name = name
        self.age = age

c = Constructor("krishna",1000)

        
