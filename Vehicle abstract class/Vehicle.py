from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def fuel(self):
        pass

    @abstractmethod
    def model(self):
        pass
    
    def honk(self):
        print("beep beep!")

    def mode_of_transportion(self):
        print("Road")

class Car(Vehicle):
    def __init__(self,name):
        self.name = name

    def start_engine(self):
        print("CAR ENGINE START")

    def fuel(self):
        print("Petrol")
    
    def model(self):
        print('car model is',self.name)

class Bus(Vehicle):
    def __init__(self,name):
        self.name = name

    def start_engine(self):
        print("BUS ENGINE START")

    def fuel(self):
        print("Electric charge")

    def model(self):
        print('Bus model is ',self.name)

c = Car('toyota')
c.start_engine()
c.fuel()
c.honk()
c.mode_of_transportion()
c.model()
print("\n")
b = Bus('ashok leyland')
b.start_engine()
b.fuel()
b.honk()
b.mode_of_transportion()
b.model()