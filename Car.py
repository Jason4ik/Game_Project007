from CarShop import car_dict
import random 
"""class Car:
    def __init__(self, brand, model, price, top_speed, acceleration, handling, color, horse_power):
        self.brand = brand
        self.model = model
        self.price = price
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.handling = handling 
        self.color = color
        self.horse_power = horse_power 
        self.speed = 0  """
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
        print(f"{self.brand} {self.model}".center(50, '='))
        print("Stats:")
        print(f'\tPower:        {self.horse_power}hp')
        print(f'\tTop speed:    {self.top_speed} km/h')
        print(f'\t0-100km/h:    {self.acceleration}s')
        print(f'\tHandling:     {self.handling}')
        print(f'\tColor:        {self.color}')
        print(f'\tPrice:        {self.price}$')
        print('='*50)

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
                            
car = Car("Aston Martin DB9")
car.get_info()
car.start()
car.speed_up(50)
car.speed_down(10)
car.stop()
car.tuning(['engine', 'suspension', 'Yellow'])
car.get_info()

from os import system

car_dict = {
    "Aston Martin DB9": {"make": "Aston", "model": "DB9", "top_speed": 300, "acceleration": 9, "colour": "silver", "Power": 999, "Price": 90000},
    "Audi TT": {"make": "Audi", "model": "3.2 quattro", "top_speed": 240, "acceleration": 7, "colour": "red", "Power": 470,  "Price": 20000},
    "Ford Mustang": {"make": "Ford", "model": "GT", "top_speed": 290, "acceleration": 9, "colour": "blue", "Power": 888,  "Price": 30000},
    "Lexus IS300": {"make": "Lexus", "model": "IS300", "top_speed": 310, "acceleration": 10, "colour": "white", "Power": 810,  "Price": 50000},
    "Lamborgini Gallardo": {"make": "Lamborgini", "model": "Gallardo", "top_speed": 300, "acceleration": 9, "colour": "yellow", "Power": 890, "Price": 70000},
    "Audi A4": {"make": "Audi", "model": "A4", "top_speed": 210, "acceleration": 8, "colour": "black", "Power": 720,  "Price": 25000},
    "BMW 3 Series": {"make": "BMW", "model": "3 Series", "top_speed": 250, "acceleration": 7, "colour": "green", "Power": 780,  "Price": 50000},
    "Mercedes-Benz CLK500": {"make": "Mercedes-Benz", "model": "CLK500", "top_speed": 280, "acceleration": 9, "colour": "gray", "Power": 800,  "Price": 25000},
    "Lexus ES": {"make": "Lexus", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "silver", "Power": 730,  "Price": 40000},
    "Mazda RX-7": {"make": "Mazda", "model": "RX-70", "top_speed": 210, "acceleration": 7, "colour": "red", "Power": 740,  "Price": 45000},
    "Pontiac GTO": {"make": "Pontiac", "model": "ES", "top_speed": 210, "acceleration": 7, "colour": "blue", "Power": 660,  "Price": 50000},
    "Mazda 6": {"make": "Mazda", "model": "6", "top_speed": 260, "acceleration": 8, "colour": "white", "Power": 800, "Price": 35000},
    "Toyota Supra": {"make": "Toyota", "model": "Supra", "top_speed": 200, "acceleration": 6, "colour": "yellow", "Power": 600, "Price": 20000},
    "BMW M3 GTR": {"make": "BMW", "model": "M3 GTR", "top_speed": 230, "acceleration": 7, "colour": "gold", "Power": 730, "Price": 40000},
    "Chevrolet Corvette": {"make": "Chevrolet", "model": "Corvete", "top_speed": 270, "acceleration": 7, "colour": "silver", "Power": 800, "Price": 40000},
    "Lotus Elise": {"make": "Lotus", "model": "Elise", "top_speed": 300, "acceleration": 7, "colour": "silver", "Power": 999, "Price": 34000}
}

class CarShop:
    def __init__(self):
        self.garage = {}
        self.balance = 0
        
    def car_buy(self, car_name, car_model):
        if car_name in car_dict and car_dict[car_name]['model'] == car_model:
            car = car_dict[car_name]
            if self.balance >= car['Price']:
                self.garage[car_name] = car
                self.balance -= car['Price']
                print(f"{car_name} {car_model} ({car['colour']}) has been added to the garage.")
            else:
                print("Insufficient balance.")
        else:
            print(f"{car_name} {car_model} is not available in the market.")
    
    def car_sell(self, car_name):
        if car_name in self.garage:
            car = self.garage[car_name]
            self.balance += car['Price']
            del self.garage[car_name]
            print(f"{car_name} has been sold.")
        else:
            print(f"{car_name} is not available in the garage.")

my_shop = CarShop()

my_shop.car_buy("Aston Martin", "DB9")
my_shop.car_buy("Ford Mustang", "GT")
my_shop.car_sell("Aston Martin")
my_shop.car_sell("Chevy Camaro")
