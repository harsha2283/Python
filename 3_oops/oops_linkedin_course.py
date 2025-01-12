#classes
class vehicle():
    is_machine = True

    def start_engine(self):
        print("Turn the KL15 on to start the engine")


#function to learn the class
def how_to_use_calss():
    
    #list 
    class_data=list()
    
    #class instances 
    #car object
    car : vehicle = vehicle()
    car.start_engine()
    class_data.append(car.is_machine)

    #truck object
    truck : vehicle = vehicle()
    truck.is_machine = False
    truck.start_engine()
    class_data.append(truck.is_machine)

    #Modifying the variable which is the class directly will impact the next instance of the class
    vehicle.is_machine = False
    class_data.append(vehicle.is_machine)

    #bike object 
    bike : vehicle = vehicle()
    bike.start_engine()
    class_data.append(bike.is_machine)

    print(class_data)

#function with multiple instances of the classes
how_to_use_calss()