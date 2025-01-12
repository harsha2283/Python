#  _1 Operator Overloading means giving extended meaning beyond their predefined operational meaning.
'''
This below example is taken from the below link
https://www.programiz.com/python-programming/operator-overloading
'''

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other_object):
        x = self.x + other_object.x
        y = self.y + other_object.y
        return Point(x, y)
    
p1 = Point(1,2)
p2 = Point(3,4)

#This statmment calls the __add__() method 
p3 = p1 + p2
        
print((p3.x, p3.y))