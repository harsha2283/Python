#--------------------------------------------------------------------------------------#
#                           concept was learnt from                                    #
#      https://pythonsimplified.com/start-using-annotations-in-your-python-code/
#                                                                                      #
#--------------------------------------------------------------------------------------#


#Syntax 
# def func(a: <expression>, b: <expression>) -> <expression>:
#     function body 

#function with annotations usage [Function Annotations]
def func(num1: int, num2: float) -> float:
    return num1+num2

#to check the annotations of a function specify the function and then use the DUNDER method annotations
print(func.__annotations__)
print(func(20, 20.5))

#variable with annotations usage [Variable Annotations]
name: str = "Harsha"
age: int = 23

#usage of simple Dunder method annotations will list out all the global variables types
print(__annotations__)