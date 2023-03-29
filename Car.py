from CarShop import car_dict
class Car:
    def __init__(self, brand, model, price, top_speed, acceleration, handling, color, horse_power):
        self.brand = brand
        self.model = model
        self.price = price 
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.handling = handling 
        self.color = color
        self.horse_power = horse_power 
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
                            
car = Car("Mercedes-Benz", "s600", 100000, 250, 2.5, 7, "Black", 500)
car.get_info()
car.start()
car.speed_up(50)
car.speed_down(10)
car.stop()
car.tuning(['engine', 'suspension', 'Yellow'])
car.get_info()

