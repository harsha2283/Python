'''
Can we limit the creation of the number of instances for a object? 
know more in the below website 
https://www.programiz.com/article/python-self-why
'''

class Sqpoint:
    Max_instance_can_be_created = 4
    Instances_created_so_far = 0
    def __new__(cls,*args,**kwargs):
        if (cls.Instances_created_so_far >= cls.Max_instance_can_be_created):
            raise ValueError(f"The instances limit is exceeded. The maximium instaces that could be created are {cls.Instances_created_so_far}")
        cls.Instances_created_so_far += 1

        return super().__new__(cls)
    
    def __init__(self, name:str):
        print(f"init function is called and a instance is created")
        self.name = name


p1 = Sqpoint("square1")
p2 = Sqpoint("square2")
p3 = Sqpoint("square3")
p4 = Sqpoint("square4")

#if we create this instance then we get a programming error sicne the limit of creating instaces is exceeded
p5 = Sqpoint("square5")