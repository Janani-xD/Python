# Interface Segregation Principle

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")

    def stop_engine(self):
        print("Car Engine Stopped")


class Boat(Vehicle):
    def start_engine(self):
        print("Boat Engine Started")

    def stop_engine(self):
        print("Boat Engine Stopped")

def test_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()

car = Car()
boat = Boat()
test_vehicle(car)
test_vehicle(boat
             )
# my_car = Car()
# my_boat = Boat()
# my_car.start_engine()
# my_car.stop_engine()
# my_boat.start_engine()
# my_boat.stop_engine()