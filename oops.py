# class and object

class Car:
    total_calls=0
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        Car.total_calls+=1

    def __str__(self):
        return f"Model -> {self.model} & Brand -> {self.brand}, {Car.total_calls}"
    
Maruti= Car("maruti","new")
print(Maruti)

# Inheritance

class ElectricCar(Car):
    def __init__(self,model,brand,battery):
        super().__init__(model,brand)
        self.battery=battery
    
    def __str__(self):
        return f'Model->{self.model} , Brand->{self.brand} , Battery->{self.battery}, {Car.total_calls}'
    
ec=ElectricCar("ola","good","85kwh")
print(ec)

#calculate total no of objects created
print(Car.total_calls)

#Encapsulation

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary #private 

    def __str__(self) -> None:
        return f"Employee Name->{self.name} and salary->{self.__salary}" 
    
    def get_Salary(self):
        return (self.__salary)
    
    def set_salary(self,salary):
        self.__salary=salary

satyam=Employee("satyam","10l")
print(satyam)    

# print(satyam.name)
#print(satyam.__salary) #cannot access private member salary

print(satyam.get_Salary())

#static methods (which acn be directly accesed by class)

class Laptop:

    def __init__(self,brand):
        self.brand=brand


    @staticmethod
    def use():
        return f"laptops are used for educational purposes"
    
    def __str__(self) -> str:
        return "{self.brand}"
lenovo=Laptop("Lenovo")
apple=Laptop("apple")
print(lenovo.use()) #can be  accesed through objects also
print(apple.use())  #can be  accesed through objects also
print(Laptop.use()) #can be  accesed through CLASSES also



















