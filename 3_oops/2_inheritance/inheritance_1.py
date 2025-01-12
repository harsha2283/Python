#--------------------------------------------------------------------------------------#
#                           concept was learnt from                                    #
#https://www.youtube.com/watch?v=rLyYb7BFgQI&list=TLPQMzExMDIwMjTsIPV6fuUYsQ&index=2   #
#https://www.youtube.com/watch?v=Gx5qb1uHss4&list=TLPQMzExMDIwMjTsIPV6fuUYsQ&index=1   #
#                                                                                      #
#--------------------------------------------------------------------------------------#

#parent Class
class Bird():

#Annotations 
#variable:type of data it has to store

    def __init__(self, bird_name:str, flight:bool, Region:str) -> None:
        self.bird_name = bird_name
        self.flight = flight
        self.Region = Region

    #Method - 1
    def fly_info(self):
        if self.flight == True:
            print(f"{self.bird_name} can fly")
        elif self.flight == False:
            print(f"{self.bird_name} cannot fly")
        else:
            print(f"This following argument {self.flight} is not valid")
        
    #Method - 2
    def Region_info(self):
        if self.Region != None:
            print(f"{self.bird_name} belongs to {self.Region}")
        else:
            print(f"Region of the {self.bird_name} bird is not defined")

    #dunder Method [dunder method - double under score method]
    def __str__(self) -> str:
        return f'Dunder - __str__ - This class is a parent class has not inherited data'
    
    def __repr__(self) -> str:
        return f'Bird(bird_name = "{self.bird_name}", flight = {self.flight}, Region = "{self.Region}")'


#child class - 1
# 1 - Single inheritance
class Dragon(Bird):

    def __init__(self, bird_name:str, flight:bool, Region:str, Species:str) -> None:
        self.Species = Species

        #invoking the __init__ of the parent class 
        # Bird.__init__(self, bird_name, flight, Region)
        super().__init__(bird_name, flight, Region)

    def species_info(self) -> None:
        print(f"The dragon belongs to species {self.Species}")

    #dunder Method [dunder method - double under score method]
    def __str__(self) -> str:
        return f'Dunder - __str__ - This class is a child class and inherited from the base class "Bird"'
    
    def __repr__(self) -> str:
        return f'Dragon(bird_name = "{self.bird_name}", flight = {self.flight}, Region = "{self.Region}", Species = "{self.Species}")'

#Notes : if any of the dunder methods missed in the child class and the method exist in the base/parent class then the method will return the data from the base class 

#child class - 2 [with properties of base and child class - 1]
# 2 - Multi level inheritance
class AnimalKingdom(Dragon, Bird):
    
    def __init__(self, bird_name: str, flight: str, Region: str, Species: str, aging:int) -> None:

        self.aging = aging
        #invoking the attributes of the base and child class - 1
        super().__init__(bird_name, flight, Region, Species)

    def animal_kingdom_info(self):
        if self.flight == True:
            print(f'The bird name is {self.bird_name}. it can fly and belongs to the species {self.Species}. it"s fossils dating goes {self.aging}years back. Fossils were found in {self.Region}')
        elif self.flight == False:
            print(f'The bird name is {self.bird_name}. it cannot fly and belongs to the species {self.Species}. it"s fossils dating goes {self.aging}years back. Fossils were found in {self.Region}')

    #dunder Method [dunder method - double under score method]
    def __str__(self) -> str:
        return f'Dunder - __str__ - This class is inherited from the base class "Bird" and child class - 1 "Dragon"'
    
    def __repr__(self) -> str:
        return f'Dragon(bird_name = "{self.bird_name}", flight = {self.flight}, Region = "{self.Region}", Species = "{self.Species}", aging = "{self.aging})'
    
#class which is inheritated from a parent class
# 1 - Single inheritance
dragon_0:Dragon = Dragon("dragon", True, "Westoros" , "dragonet")

print((dragon_0))
print(repr(dragon_0))

# 2 - Multi level inheritance
dragon_1:AnimalKingdom = AnimalKingdom("Dragon", True, "winterfell", "fire dragon", 1000)

print(dragon_1)
print(repr(dragon_1))




