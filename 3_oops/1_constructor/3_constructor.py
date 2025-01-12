'''
why self used in the class? 
know more in the below website 
https://www.programiz.com/article/python-self-why
'''


class EngineState:
    
    def __init__(self, vehicle, engine_type, condition):
        self.vehicle = vehicle
        self.engine_type = engine_type
        self.condition = condition

    def info(self):
        print(f"Data from info() method: The Vehicle is {self.vehicle} and it's engine is of type {self.engine_type} and it is {self.condition}")

    #note: if a dunder method __str__ is not avaible then the class will deliver the data in the repr method

    def __repr__(self) -> str:
        return f'EngineState(vehicle : "{self.vehicle}, engine_type : {self.engine_type}", condition : "{self.condition}")'

#class - Instance
# varaible or a class : variables type or the original class.
Engine_state_1 : EngineState = EngineState("Porsche", "V12", "Not Working")

Engine_state_1.info()
print(Engine_state_1)
print(repr(Engine_state_1))
