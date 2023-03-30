from os import system
import time

car_dict = {
    "Aston Martin DB9": {"make": "Aston Martin", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "silver", "Power": 999, "Price": 90000},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red", "Power": 470,  "Price": 20000},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "Power": 888,  "Price": 30000},
    "Lexus IS300": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white", "Power": 810,  "Price": 50000},
    "Lamborgini Gallardo": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow", "Power": 890, "Price": 70000},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 210, "acceleration": 8, "colour": "black", "Power": 720,  "Price": 25000},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 250, "acceleration": 7, "colour": "green", "Power": 780,  "Price": 50000},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "gray", "Power": 800,  "Price": 25000},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "silver", "Power": 730,  "Price": 40000},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-7", "top_speed": 210, "acceleration": 7, "colour": "red", "Power": 740,  "Price": 45000},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue", "Power": 660,  "Price": 50000},
    "Mazda 6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white", "Power": 800, "Price": 35000},
    "Toyota Supra": {"make": "Toyota", "model": "Supra", "top_speed": 200, "acceleration": 6, "colour": "yellow", "Power": 600, "Price": 20000},
    "BMW M3 GTR": {"make": "BMW", "model": "M3 GTR", "top_speed": 230, "acceleration": 7, "colour": "gold", "Power": 730, "Price": 40000},
    "Chevrolet Corvette": {"make": "Chevrolet", "model": "Corvette", "top_speed": 270, "acceleration": 7, "colour": "silver", "Power": 800, "Price": 40000},
    "Lotus Elise": {"make": "Lotus", "model": "Elise", "top_speed": 300, "acceleration": 7, "colour": "silver", "Power": 999, "Price": 34000}
}

class CarShop:
    def __init__(self):
        self.garage = {}
        
    def car_buy(self, car_name, car_model, shop_money: int) -> None:
        if car_name in car_dict and car_dict[car_name]['model'] == car_model:
            car = car_dict[car_name]
            if shop_money >= car['Price']:
                self.garage[car_name] = car
                shop_money -= car['Price']
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
            return car['Price']
        else:
            print(f"{car_name} is not available in the Garage.")



my_shop = CarShop()

my_shop.car_buy("Aston Martin DB9", "DB9", shop_money=90000)
my_shop.car_buy("Chevrolet Corvette", "Corvette", shop_money=40000)
my_shop.car_sell("Aston Martin DB9")
my_shop.car_sell("Chevrolet Corvette")