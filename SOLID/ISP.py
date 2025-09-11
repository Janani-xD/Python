# Interface Segregation Principle
# ISP states that the user should not have to use an interface , ie not using an interface  if they do not want to
# Both car and Boat inherit vehicle and they extend the start_engine and stop engine , hence giving us control of
# what we want in our appplication
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

def test_vehicle(vehicle):   # This function does not care about what object it it
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