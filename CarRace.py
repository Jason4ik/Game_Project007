import random
import time
from CarShop import car_dict

maps = {
    "Florida": {"length": 20.55, "difficulty": "easy"},
    "Nürnburgring": {"length": 20.88, "difficulty": "medium"},
    "Monaco": {"lenght": 31.63, "difficulty": "hard"}
}
car_dict1 = list(car_dict)
difficulty = []
easy = []
medium = []
hard = []

class CarRace:
    def __init__(self):
        self = self

    

    def enemies(self,enemies):
        self.enemies = enemies
        enemies = random.choice(car_dict.keys())
        return enemies
    

    def Start_Game(self):
        print(f'Choose your game:"{list(maps)}')
        for key in maps:
            difficulty.append(maps[key]["difficulty"])
        print("                    ",difficulty)
        print("                         1        2       3")
        choice = input("")
        if choice == "1":
            print(f'Lets drive in Florida{maps["Florida"]}')
            print()
            easy.append(random.choice(car_dict1))
            print(f'Your enemie will be {easy}')
            #choice = input(f'Choose your car:{CarShop(self.garage)}')
            
        elif choice == "2":
            print(f'Lets drive in Nürnburgring{maps["Nürnburgring"]}')
            print()
            for i in range(2):
                medium.append(random.choice(car_dict1))
            print(f'Your enemies will be{medium} ')

        elif choice == "3":
            print(f'Lets drive in Monaco{maps["Monaco"]}')
            print()
            for i in range(3):
                hard.append(random.choices(car_dict1))
            print(f'Your enemies will be {hard}')
        else:
            print("Wrong input my friend")
        print()
        input("Press Enter to continue")

        for i in range(1,4):
            time.sleep(1)
            print(i)
            if i == 3:
                time.sleep(1)
                print("GO!")
        
        print("Oh NO! Your enemy is far ahead you need to accelerate...")
        time.sleep(0.5)
        print("Press W to accelerate")
        
    
    



        

        


my_game = CarRace()

my_game.Start_Game()
