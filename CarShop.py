from os import system
import time

car_dict = {
    "Aston Martin DB9": {"make": "Aston", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "silver", "power": 999, "price": 90000},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red", "power": 470,  "price": 20000},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "power": 888,  "price": 30000},
    "Lexus IS300": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white", "power": 810,  "price": 50000},
    "Lamborgini Gallardo": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow", "power": 890, "price": 70000},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 210, "acceleration": 8, "colour": "black", "power": 720,  "price": 25000},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 250, "acceleration": 7, "colour": "green", "power": 780,  "price": 50000},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "gray", "power": 800,  "price": 25000},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "silver", "power": 730,  "price": 40000},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-7", "top_speed": 210, "acceleration": 7, "colour": "red", "power": 740,  "price": 45000},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue", "power": 660,  "price": 50000},
    "Mazda 6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white", "power": 800, "price": 35000},
    "Toyota Supra": {"make": "Toyota", "model": "Supra", "top_speed": 200, "acceleration": 6, "colour": "yellow", "power": 600, "price": 20000},
    "BMW M3 GTR": {"make": "BMW", "model": "M3 GTR", "top_speed": 230, "acceleration": 7, "colour": "gold", "power": 730, "price": 40000},
    "Chevrolet Corvette": {"make": "Chevrolet", "model": "Corvette", "top_speed": 270, "acceleration": 7, "colour": "silver", "power": 800, "price": 40000},
    "Lotus Elise": {"make": "Lotus", "model": "Elise", "top_speed": 300, "acceleration": 7, "colour": "silver", "power": 999, "price": 34000}
}

class CarShop:
    def __init__(self):
        self.garage = {"Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "power": 888,  "price": 30000}}

    def car_buy(self, car_name, car_model, shop_money: int) -> None:
        if car_name in car_dict and car_dict[car_name]['model'] == car_model:
            car = car_dict[car_name]
            if shop_money >= car['price']:
                self.garage[car_name] = car
                shop_money -= car['price']
                print(f"{car_name} {car_model} ({car['colour']}) has been added to the Garage.")
            else:
                print("Insufficient balance.")
        else:
            print(f"{car_name} {car_model} Sorry Bro... It's not in the Shop.")
    
    def car_sell(self, car_name) -> int:
        if car_name in self.garage:
            car = self.garage[car_name]
            del self.garage[car_name]
            print(f"{car_name} has been sold.")
            return car['price']
        else:
            print(f"{car_name} is not available in the Garage.")

class Garage:
    def __init__(self, car_shop):
        self.car_shop = car_shop

    def show_all_cars(self):
        print("Available cars in the Garage:")
        for car_name in self.car_shop.garage:
            print(f"- {car_name}")

my_car_shop = CarShop()

my_car_shop.car_buy("Audi TT", "3.2 quattro", 50000)
my_car_shop.car_buy("Lamborgini Gallardo", "Gallardo", 80000)

my_car_shop.car_sell("Audi TT")

my_garage = Garage(my_car_shop)

my_garage.show_all_cars()