from os import system
import time
# from CarShop import CarShop
# from Car import Car
# from CarRace import CarRace


class Driver:
    def __init__(self, name: str, gender:str, age: int, glasses: str, gloves: str, shoes: str):
        self.name = name
        self.age = age
        self.glasses = glasses
        self.gloves = gloves
        self.shoes = shoes
        self.gender = gender
        self.__levpassel = 0
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

class Game:
    _instance = None
    def __init__(self):
        self.drivers = []
        self.play_music()
        print('WELCOME TO NEED FOR SLEEP'.center(50, "="))
        print()
        print("Seems, like you new here, bro, you have to create your own driver.")
        self.driver_creation()


    def driver_creation(self):
        system('clear')
        name = input('Insert the name of your driver: ')
        gender = input('Choose the gender of your driver: ')
        age = int(input("Insert age of your driver: "))
        glasses = input('Choose the glasses of a driver[black/transparent]: ')
        gloves = input('Choose the gloves of a driver[black leather/red leather/rose leather]: ')
        shoes = input("Choose the shoes of a driver[sneakers/black boots]: ")
        self.drivers.append(Driver(name, gender, age, glasses, gloves, shoes))

    def menu(self):
        system('clear')
        print('Choose an action'.center(50, ' '))
        choice = input("""[1] - New game""")
        # while 

        


    def start_game(self):
        pass

    def play_music(self):
        # while True:
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    game = Game()