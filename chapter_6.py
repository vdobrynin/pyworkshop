# 
# class Car:
#     # runs = False
#     runs = True

#     def start(self):
#         if self.runs:
#             print("Car is started. Vroom vroom! :-)")
#         else:
#             print("Car is broken :-(")

# my_car = Car()
# print(f"My car runs: {my_car.runs}")
# my_car.start()

# class Car:
#     runs = True

#     def start(self):
#         if self.runs:
#             print("Car is started. Vroom vroom !!!")
#         else:
#             print("Car is broken :-(")

# my_car = Car()
# my_car.runs = False
# my_car.start()

# my_other_car = Car()
# my_other_car.start()

# class Car:
#     runs = True
#     number_of_wheels = 4

#     @classmethod
#     def get_number_of_wheels(cls):
#         return cls.number_of_wheels

#     def start(self):
#         if self.runs:
#             print("Car is started. Vroom vroom !!")
#         else:
#             print("Car is broken :-(")

# my_car = Car()
# print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# # Of course, we can override this in our instance:
# my_car.number_of_wheels = 6

# # And when we access our new instance variable:
# print(f"My car has {my_car.number_of_wheels} wheels.")

# # But, when we call our class method on our instance:
# print(f"My car has {my_car.get_number_of_wheels()} wheels.")

# class Car:
#     runs = True

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start(self):
#         if self.runs:
#             print(f"Your {self.make} {self.model} is started. Vroom vroom!")
#         else:
#             print(f"Your {self.make} {self.model} is broken :(")

# my_car = Car("Ford", "Thunderbird")
# my_car.start()

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

my_car = Car("Ford", "Thunderbird")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")

# my_ints = [int(str_num) for str_num in ["1", "2", "3"]]
# print(my_ints)
# # [1, 2, 3]

# # chapter_6.py
# from vehicle import Vehicle, Car

# my_car = Car("Ford", "Thunderbird")
# print(f"my_car is type {type(my_car)}")
# print(f"my_car uses {my_car.fuel}")

# print(f"my_car is a Car: {isinstance(my_car, Car)}")
# print(f"my_car is a Vehicle: {isinstance(my_car, Vehicle)}")
# print(f"Car is a subclass of Vehicle: {issubclass(Car, Vehicle)}")

# # chapter_6.py
from vehicle import Truck
 
my_truck = Truck("Ford", "F350")
print(f"my_truck is type {type(my_truck)}")
print(f"my_truck uses {my_truck.fuel}")
print(f"my_truck has {my_truck.number_of_wheels} wheels") 