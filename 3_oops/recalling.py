class Employee():
    def __init__(self, name:str, age:int, degree:str):
        self.name = name
        self.age = age
        self.degree = degree

    def employee_salary_calculation(self):
        if self.age > 20:
            self.salary_percentage = self.age/20
            self.salary = self.salary_percentage*100000
            print(f"{self.name}'s age is {self.age}. So, the salary is {self.salary}")
        else:
            print(f"{self.name}'s age is {self.age}. So, this profile is eligible for the internship")

    def __str__(self):
        return f'Dunder - __str__ - This is the main class which have the following methods: \n1. employee_salary_calculation()\n Dunder Methods: 1.__str__()\n2.__repr__()'
    
    def __repr__(self):
        return f"Dunder - __repr__ - "
