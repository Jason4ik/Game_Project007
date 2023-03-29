import random
from CarShop import car_dict
maps = {
    "Florida": {"length": 20.55, "difficullty": "easy"},
    "Nürnburgring": {"length": 20.88, "difficulty": "medium"},
    "Monaco": {"lenght": 31.63, "difficulty": "hard"}
}
enemys = random.randint(1,len(car_dict))

class CarRace:
    def __init__(self):
        self.game = self
    

    def Start_Game(self):
        print(f'Choose your game:"{maps}')
        choice = input("")
        if choice == "Florida".lower() or "Florida".upper():
            print(f'Lets drive in Florida{maps["Florida"]}')
        elif choice == "Nürnburgring".lower() or "Nürnburgring".upper():
            print(f'Lets drive in Nürnburgring{maps["Nürnburgring"]}')
        elif choice == "Monaco".lower() or "Monaco".upper():
            print(f'Lets drive in Monaco{maps["Monaco"]}')
        else:
            print("Wrong input my friend")

    



        

        


my_game = CarRace()
my_game.Start_Game()


                

            
