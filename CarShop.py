from os import system
import time
from Car import Car

car_dict = {
    "Aston Martin": {"make": "Aston Martin", "model": "DB9", "top_speed": 300, "xp": 9},
    "Honda Accord": {"make": "Lexus", "model": "Accord", "top_speed": 115, "acceleration": 6},
    "Ford Mustang": {"make": "Ford", "model": "Mustang", "top_speed": 150, "acceleration": 8},
    "Chevy Camaro": {"make": "Chevy", "model": "Camaro", "top_speed": 140, "acceleration": 7},
    "Nissan Maxima": {"make": "Nissan", "model": "Maxima", "top_speed": 125, "acceleration": 6},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 135, "acceleration": 7},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 140, "acceleration": 8},
    "Mercedes-Benz C-Class": {"make": "Mercedes-Benz", "model": "C-Class", "top_speed": 145, "acceleration": 9},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 130, "acceleration": 6},
    "Mazda6": {"make": "Mazda", "model": "6", "top_speed": 120, "acceleration": 5}
}

class CarShop:
    def __init__(self):
        self.inventory = {}
        
    def car_buy(self, car_name, car_model):
        if car_name in car_dict and car_dict[car_name]['model'] == car_model:
            car = car_dict[car_name]
            self.inventory[car_name] = car
            print(f"{car_name} {car_model} has been added to the inventory.")
        else:
            print(f"{car_name} {car_model} is not available in the car_dict.")
    
    def car_sell(self, car_name):
        if car_name in self.inventory:
            del self.inventory[car_name]
            print(f"{car_name} has been sold.")
        else:
            print(f"{car_name} is not available in the inventory.")


my_shop = CarShop()
my_shop.car_buy("Aston Martin", "DB9")
my_shop.car_buy("Ford Mustang", "GT")

my_shop = CarShop()

my_shop.car_buy("Aston Martin", "DB9")
my_shop.car_buy("Ford Mustang", "GT")
my_shop.car_sell("Aston Martin")
my_shop.car_sell("Chevy Camaro")