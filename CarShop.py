from os import system
import time
from Car import Car

car_dict = {
    "Aston Martin": {"make": "Aston Martin", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "silver"},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red"},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue"},
    "Lexus": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white"},
    "Lamborgini": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow"},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 135, "acceleration": 8, "colour": "black"},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 140, "acceleration": 7, "colour": "green"},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "gray"},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "silver"},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-70", "top_speed": 210, "acceleration": 7, "colour": "red"},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue"},
    "Mazda6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white"}
}

class CarShop:
    def __init__(self):
        self.garage = {}
        
    def car_buy(self, car_name, car_model):
        if car_name in car_dict and car_dict[car_name]['model'] == car_model:
            car = car_dict[car_name]
            self.garage[car_name] = car
            print(f"{car_name} {car_model} ({car['colour']}) has been added to the garage.")
        else:
            print(f"{car_name} {car_model} is not available in the car_dict.")
    
    def car_sell(self, car_name):
        if car_name in self.garage:
            del self.garage[car_name]
            print(f"{car_name} has been sold.")
        else:
            print(f"{car_name} is not available in the garage.")


my_shop = CarShop()

my_shop.car_buy("Aston Martin", "DB9")
my_shop.car_buy("Ford Mustang", "GT")

my_shop = CarShop()

my_shop.car_buy("Aston Martin", "DB9")
my_shop.car_buy("Ford Mustang", "GT")
my_shop.car_sell("Aston Martin")
my_shop.car_sell("Chevy Camaro")
