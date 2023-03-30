from os import system
import time

car_dict = {
    "Aston Martin DB9": {"make": "Aston", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "purple", "power": 999, "price": 90000},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red", "power": 470,  "price": 20000},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "power": 888,  "price": 30000},
    "Lexus IS300": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white", "power": 810,  "price": 50000},
    "Lamborgini Gallardo": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow", "power": 890, "price": 70000},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 210, "acceleration": 8, "colour": "black", "power": 720,  "price": 25000},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 250, "acceleration": 7, "colour": "green", "power": 780,  "price": 50000},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "cyan", "power": 800,  "price": 25000},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "cyan", "power": 730,  "price": 40000},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-7", "top_speed": 210, "acceleration": 7, "colour": "red", "power": 740,  "price": 45000},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue", "power": 660,  "price": 50000},
    "Mazda 6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white", "power": 800, "price": 35000},
    "Toyota Supra": {"make": "Toyota", "model": "Supra", "top_speed": 200, "acceleration": 6, "colour": "yellow", "power": 600, "price": 20000},
    "BMW M3 GTR": {"make": "BMW", "model": "M3 GTR", "top_speed": 230, "acceleration": 7, "colour": "black", "power": 730, "price": 40000},
    "Chevrolet Corvette": {"make": "Chevrolet", "model": "Corvette", "top_speed": 270, "acceleration": 7, "colour": "black", "power": 800, "price": 40000},
    "Lotus Elise": {"make": "Lotus", "model": "Elise", "top_speed": 300, "acceleration": 7, "colour": "purple", "power": 999, "price": 34000}
}

class CarShop:
    def __init__(self):
        self.garage = {"Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "power": 888,  "price": 30000}}

    def car_buy(self, car_name, car_model, shop_money: int) -> None:
        car = car_dict.get(car_name)
        if car and car["model"] == car_model:
            if car_name not in self.garage:
                if shop_money >= car["price"]:
                    self.garage[car_name] = car
                    shop_money -= car["price"]
                    car_color = car["colour"].lower()
                    color_code = {
                        "black": "\033[0;30m",
                        "red": "\033[0;31m",
                        "green": "\033[0;32m",
                        "yellow": "\033[0;33m",
                        "blue": "\033[0;34m",
                        "purple": "\033[0;35m",
                        "cyan": "\033[0;36m",
                        "white": "\033[0;37m"
                    }.get(car_color, "\033[0m...")
                    print(f"{color_code}{car_name}{color_code} added to the garage!")
                else:
                    print("Not enough money to buy the car!")
            else:
                print("Car is already in the garage!")
        else:
            print("Car not found in the dictionary!")

    def car_sell(self, car_name) -> int:
        if car_name in self.garage:
            car = self.garage[car_name]
            del self.garage[car_name]
            print(f"{car_name} has been sold.")
            return car['price']
        else:
            print(f"{car_name} is not available in the Garage.")
    
    def show_car_dict(self):
        for car_name, car_details in self.garage.items():
            print(f"{car_name}: {car_details}")


class Garage:
    def __init__(self, car_shop):
        self.car_shop = car_shop

    def show_all_cars(self):
        print("Available cars in the Garage:", end=" ")
        for car_name in self.car_shop.garage:
            car_color = self.car_shop.garage[car_name]["colour"].lower()
            color_code = {
                "black": "\033[0;30m",
                "red": "\033[0;31m",
                "green": "\033[0;32m",
                "yellow": "\033[0;33m",
                "blue": "\033[0;34m",
                "purple": "\033[0;35m",
                "cyan": "\033[0;36m",
                "white": "\033[0;37m"
            }.get(car_color, "\033[0m")
            print(f"{color_code}- {car_name}\033[0m", end=", ")
        print()

my_car_shop = CarShop()

my_car_shop.car_buy("Audi TT", "3.2 quattro", 50000)
my_car_shop.car_buy("Lamborgini Gallardo", "Gallardo", 80000)
my_car_shop.car_buy("Lexus ES", "ES", 80000)
my_car_shop.car_buy("BMW M3 GTR", "M3 GTR", 80000)
my_car_shop.car_sell("Audi TT")

my_garage = Garage(my_car_shop)

my_garage.show_all_cars()

