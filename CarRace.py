import random
import time
from CarShop import car_dict
import CarShop

maps = {
    "Florida": {"length": 20.55, "difficulty": "easy"},
    "Nürnburgring": {"length": 20.88, "difficulty": "medium"},
    "Monaco": {"lenght": 31.63, "difficulty": "hard"}
}

class CarRace:
    def __init__(self):
        self = self

        self.car_dict1 = list(car_dict)
        self.difficulty = []
        self.easy = []
        self.medium = []
        self.hard = []
        self.my_car = []
        self.my_car_speed=[]

    # def __str__(self):
    #     return str(garage)

    def enemies(self,enemies):
        self.enemies = enemies
        enemies = random.choice(car_dict.keys())
        return enemies
    
    def choose_car(self,garage:dict):
        
        print(f'You can choose between this cars: ')
        for a in garage.keys():
            print(a)
        choice = input(f'Choose your Car') 
        self.my_car.append(garage[choice])
        
        input("Press Enter to continue")

    

    def Start_Game(self):
        print(f'Choose your game:"{list(maps)}')
        for key in maps:
            self.difficulty.append(maps[key]["difficulty"])
        print("                    ",self.difficulty)
        print("                         1        2       3")
        choice = input("")
        if choice == "1":
            print(f'Lets drive in Florida{maps["Florida"]}')
            print()
            self.easy.append(random.choice(self.car_dict1))
            print(f'Your enemie will be {self.easy}')
            #choice = input(f'Choose your car:{CarShop(self.garage)}')
            
        elif choice == "2":
            print(f'Lets drive in Nürnburgring{maps["Nürnburgring"]}')
            print()
            for i in range(2):
                self.medium.append(random.choice(self.car_dict1))
            print(f'Your enemies will be{self.medium}')

        elif choice == "3":
            print(f'Lets drive in Monaco{maps["Monaco"]}')
            print()
            for i in range(3):
                self.hard.append(random.choices(self.car_dict1))
            print(f'Your enemies will be {self.hard}')
        else:
            print("Wrong input my friend")
        print()
        
        CarRace.choose_car(CarShop.garage,choice)
        for i in range(1,4):
            time.sleep(1)
            print(i)
            if i == 3:
                time.sleep(1)
                print("GO!")
        
        print("Oh NO! Your enemy is far ahead you need to accelerate...")
        choice = input("PRESS W TO SPEED UP")
        if choice == "w" or "W":

            time.sleep(0.5)
        



        
    
    



        

        


my_game = CarRace()

my_game.Start_Game()
