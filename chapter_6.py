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

# chapter_6.py

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom !!!")
        else:
            print("Car is broken :-(")

my_car = Car()
my_car.runs = False
my_car.start()

my_other_car = Car()
my_other_car.start()
