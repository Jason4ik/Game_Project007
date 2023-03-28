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

    def get_info(self):
        print(f"{self.brand} {self.model}".center(50, '='))
        print("Stats:")
        print(f'\tPower:        {self.horse_power}hp')
        print(f'\tTop speed:    {self.top_speed}km/h')
        print(f'\t0-100km/h:    {self.acceleration}s')
        print(f'\tHandling:     {self.handling}')
        print(f'\tColor:        {self.color}')
        print(f'\tPrice:        {self.price}$')

    def start(self):
        print(f"")

    def stop(self):
        pass   

    def tunning(self):
        pass


car = Car("Mercedes-Benz", "s600", 100000, 250, 2.5, 7, "Black", 500)
car.get_info()
