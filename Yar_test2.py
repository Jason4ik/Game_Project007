import random
import time
from playsound import playsound
from os import system

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

class Car:
    def __init__(self, car_name):
        car = car_dict[car_name]
        self.brand = car['make']
        self.model = car['model']
        self.price = car['price']
        self.top_speed = car['top_speed']
        self.acceleration = car['acceleration']
        self.handling = random.randrange(1, 10)
        self.color = car['colour']
        self.horse_power = car['power']
        self.speed = 0 

    def get_info(self):
        print(c(f"{self.brand} {self.model}".center(50, '=')).blue.on_yellow)
        print("Stats:")
        print(f'\tPower:        {self.horse_power}hp')
        print(f'\tTop speed:    {self.top_speed} km/h')
        print(f'\t0-100km/h:    {self.acceleration}s')
        print(f'\tHandling:     {self.handling}')
        print(f'\tColor:        {self.color}')
        print(f'\tPrice:        {self.price}$')
        print(c('='*50).blue.on_yellow)

    def start(self):
        print(f"The car has been started and ready for race. Wrm-Wrm...")

    def speed_up(self, speed_delta):
        new_speed = self.speed + speed_delta
        if new_speed <= self.top_speed:
            self.speed = new_speed
            print(f"The car has accelerated to {self.speed} km/h.")
        else:
            self.speed = self.top_speed
            print(f"The car has reached its top speed of {self.top_speed} km/h.")

    def speed_down(self, speed_delta):
        new_speed = self.speed - speed_delta
        if new_speed >= 0:
            self.speed = new_speed
            print(f"The car has slowed down to {self.speed} km/h.")
        else:
            self.speed = 0
            print("The car has come to a complete stop.")

    def stop(self):
        self.speed = 0
        print("The car has come to a complete stop.")

    def tuning(self, upgrades):
        print(c(text2art("PIMP MY RIDE Studio is online now")).yellow.blink.dark)
        print(f"Hey hey hey, it's X to the Z Xzibit, and I'm ready to show you some love by pimping your ride! Let`s PIMP your Ride man!")
        colors = ["Red","Orange","Yellow","Green","Blue","Indigo","Violet","Coral"]
        for upgrade in upgrades:
            if upgrade == 'engine':
                self.horse_power *= 1.1
                self.acceleration *= 0.9
                self.top_speed *= 1.17
                print("Engine upgrade installed.")
            elif upgrade == 'suspension':
                self.handling *= 1.2
                print("Suspension upgrade installed.")
            elif upgrade in colors:
                self.color = upgrade
                self.price *= 1.05
                print("Color upgrade installed.")
            else:
                print(f"Unknown upgrade: {upgrade}")
                            
car = Car("Audi TT")
car.get_info()
car.start()
car.speed_up(50)
car.speed_down(10)
car.stop()
car.tuning(['engine', 'suspension', 'Yellow'])
car.get_info()

car_dict = {
    "Aston Martin DB9": {"make": "Aston Martin", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "silver", "power": 999, "price": 90000},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red", "power": 470,  "price": 20000},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "power": 888,  "price": 30000},
    "Lexus IS300": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white", "power": 810,  "price": 50000},
    "Lamborgini Gallardo": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow", "power": 890, "price": 70000},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 210, "acceleration": 8, "colour": "black", "power": 720,  "price": 25000},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 250, "acceleration": 7, "colour": "green", "power": 780,  "price": 50000},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "gray", "power": 800,  "price": 25000},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "silver", "power": 730,  "price": 40000},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-70", "top_speed": 210, "acceleration": 7, "colour": "red", "power": 740,  "price": 45000},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue", "power": 660,  "price": 50000},
    "Mazda 6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white", "power": 800, "price": 35000},
    "Toyota Supra": {"make": "Toyota", "model": "Supra", "top_speed": 200, "acceleration": 6, "colour": "yellow", "power": 600, "price": 20000},
    "BMW M3 GTR": {"make": "BMW", "model": "M3 GTR", "top_speed": 230, "acceleration": 7, "colour": "gold", "power": 730, "price": 40000},
    "Chevrolet Corvette": {"make": "Chevrolet", "model": "Corvete", "top_speed": 270, "acceleration": 7, "colour": "silver", "power": 800, "price": 40000},
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

class Driver:
    def __init__(self, name: str, gender: str, age: int, glasses: str, gloves: str, shoes: str):
        self.name = name
        self.age = age
        self.glasses = glasses
        self.gloves = gloves
        self.shoes = shoes
        self.gender = gender
        self.car_shop = CarShop()
        self.__level = 0
        self.__xp = 0
        self.__money = 50000

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, earnings):
        self.__money += earnings

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, xp):
        self.__xp += xp
        if self.__xp > 1000:
            self.__level += 1

    def check_stats(self):
        print(f"Driver {self.name}".center(50, '='))
        print("Stats:")
        print(f'\tAge:        {self.age}')
        print(f'\tMoney:      {self.__money}$')
        print(f'\tLevel:      {self.__level}')
        print(f'\tXP:         {self.__xp}')
        print(f'\tGlasses:    {self.glasses}')
        print(f'\tGloves:     {self.gloves}')
        print(f'\tShoes:      {self.shoes}')

