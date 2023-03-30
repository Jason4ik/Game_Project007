from os import system
import time
from CarShop import CarShop
# from Car import Car
# from CarRace import CarRace
import pygame
from art import *
from tqdm import trange


class Driver:
    def __init__(self, name: str, gender:str, age: int, glasses: str, gloves: str, shoes: str):
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

class Game:
    _instance = None
    def __init__(self):
        self.loading()
        self.drivers = []
        self.play_music()
        system('clear')
        print(text2art('''WELCOME TO
NEED 
FOR 
SLEEP'''))
        print()
        print("Seems, like you new here, bro, you have to create your own driver.")
        input("Press Enter to proceed...")
        self.driver_creation()
        self.menu()


    def driver_creation(self):
        system('clear')
        name = input('Insert the name of your driver: ')
        gender = input('Choose the gender of your driver: ')
        age = int(input("Insert age of your driver: "))
        glasses = input('Choose the glasses of a driver[black/transparent]: ')
        gloves = input('Choose the gloves of a driver[black leather/red leather/rose leather]: ')
        shoes = input("Choose the shoes of a driver[sneakers/black boots]: ")
        self.drivers.append(Driver(name, gender, age, glasses, gloves, shoes))
        print("Driver successfully created!")

    def menu(self):
        system('clear')
        choice = '1'
        while choice != 'x':
            system('clear')
            print(text2art("Main Menu"))
            choice = input("""[1] -> New game
[2] -> Check driver stats
[3] -> Check garage
[x] -> Exit the game

""")
            

    def loading(self) -> None: 
        system('clear')
        print(text2art("Loading"))
        for char in trange(100):
            time.sleep(0.01)
        time.sleep(2)
        system('clear')

    def start_game(self):
        pass

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./Riders-on-the-Storm.mp3')
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play()

    def enter_the_garage(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    game = Game()