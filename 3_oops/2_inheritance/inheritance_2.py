#-------------------------------------------------------------------#
#               concept was learnt from                             #
#     https://www.geeksforgeeks.org/types-of-inheritance-python/    #
#                                                                   #
#-------------------------------------------------------------------#

#parent class - 1
class Vegetable:

    def __init__(self, vegetable_name:str, root_type:str, edible:bool, season:str) -> None:
        self.vegetable_name = vegetable_name
        self.root_type = root_type
        self.edible = edible
        self.season = season
    
    def vegetable_info(self) -> str:
        if self.edible == True:
            return f'The vegetable name is {self.vegetable_name} and it"s roots are {self.root_type}. it is edible and mostly available in {self.season} seasons'
        elif self.edible == False:
            return f'The vegetable name is {self.vegetable_name} and it"s roots are {self.root_type}. it is not edible and mostly available in {self.season} seasons'
    
    def __str__(self) -> str:
        return f"'Vegetable' is a parent class"
    
    def __repr__(self) -> str:
        return f"Vegetable(vegetable_name : '{self.vegetable_name}', root_type : '{self.root_type}', edible : '{self.edible}', season : '{self.season}')"
    
#parent class - 2
class VegCurry:

    def __init__(self, curry_name:str, vegtables_used:list, spicy_level:int) -> None:
        self.curry_name = curry_name
        self.vegtables_used = vegtables_used
        self.spicy_level = spicy_level

    def vegcurry_info(self):
        if self.vegtables_used == None:
            return f'Name of the veg curry is {self.curry_name} and it is not made out of any veggies the spicy level out of 10 is {self.spicy_level}'
        else:
            return f'Name of the curry is {self.curry_name} and it is made of the following vegtables {self.vegtables_used}.The spicy level out of 10 is {self.spicy_level}'
        
    def __str__(self) -> str:
        return f'Vegcurry is a parent class'
    
    def __repr__(self) -> str:
        return f'VegCurry(curry_name : "{self.curry_name}", vegtables_used : "{self.vegtables_used}", spicy_level : "{self.spicy_level}")'
    

#multiple inheritance
#child class 
class CurriesMenu(Vegetable, VegCurry):
    
    def __init__(self, vegetable_name: str, root_type: str, edible: bool, season: str, curry_name: str, vegtables_used: list, spicy_level: int, items_in_menu:int) -> None:
        self.items_in_menu = items_in_menu
        #invoking the attribute of the parent class Vegetable and VegCurry
        Vegetable.__init__(self, vegetable_name, root_type, edible, season)
        VegCurry.__init__(self, curry_name, vegtables_used, spicy_level)

    def curries_menu_info(self):
        if self.edible == True:
            return f'The veg curry name is {self.curry_name} and the vegetables used are {self.vegtables_used}. The vegetable name is {self.vegetable_name} and it"s roots are {self.root_type}. it is edible and mostly available {self.season} seasons'
        elif self.edible == False:
            return f'The veg curry name is {self.curry_name} and the vegetables used are {self.vegtables_used}. The vegetable name is {self.vegetable_name} and it"s roots are {self.root_type}. it is not edible and mostly available {self.season} seasons'
    
    def __str__(self) -> str:
        return f'CurriesMenu'

    def __repr__(self) -> str:
        return f'CurriesMenu(vegetable_name : "{self.vegetable_name}", root_type : "{self.root_type}", edible : "{self.edible}", season : "{self.season}", curry_name : "{self.curry_name}", vegtables_used : "{self.vegtables_used}", spicy_level : "{self.spicy_level}", items_in_menu : "{self.items_in_menu}")'

#multiple inheritance instance 

Tomato: CurriesMenu = CurriesMenu("tomato", "Fibrious", True, "all", "tomato curry", "tomato", 5, 1)

print(Tomato.curries_menu_info())
print(Tomato.vegetable_info())
print(Tomato)
print(repr(Tomato))
