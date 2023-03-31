from os import system
import time
from CarShop import CarShop, Garage
# from Car import Car
# from CarRace import CarRace
import pygame
from art import *
from tqdm import trange
import threading
import json

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
    def money(self, new_money):
        self.__money = new_money

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, xp):
        self.__xp += xp
        if self.__xp > 1000:
            self.__level += 1

    def check_stats(self):
        system('clear')
        print(f"Driver {self.name}".center(50, '='))
        print("Stats:")
        print(f'\tAge:        {self.age}')
        print(f'\tMoney:      {self.__money}$')
        print(f'\tLevel:      {self.__level}')
        print(f'\tXP:         {self.__xp}')
        print(f'\tGlasses:    {self.glasses}')
        print(f'\tGloves:     {self.gloves}')
        print(f'\tShoes:      {self.shoes}')
        input("\nPress Enter to proceed...")

class Game:
    _instance = None
    def __init__(self):
        self.loading()
        self.driver = None
        self.songs = ['./Music/Riders-on-the-Storm.mp3', './Music/Skinnyman-Static-X.mp3', './Music/Chingy - I Do.mp3', './Music/Christopher Lawrence - Rush Hour.mp3', './Music/Goldfrapp - Ride A White Horse.mp3','./Music/Need For Speed Carbon Soundtrack - Hard Drivers.mp3']
        self.music_player_event = threading.Event()
        self.music_player = threading.Thread(target=self.play_music)
        self.music_player.start()
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

    def load_savings(self):
        pass

    def driver_creation(self):
        system('clear')
        name = input('Insert the name of your driver: ')
        gender = input('Choose the gender of your driver: ')
        age = int(input("Insert age of your driver: "))
        glasses = input('Choose the glasses of a driver[black/transparent]: ')
        gloves = input('Choose the gloves of a driver[black leather/red leather/rose leather]: ')
        shoes = input("Choose the shoes of a driver[sneakers/black boots]: ")
        self.driver = Driver(name, gender, age, glasses, gloves, shoes)
        print("Driver successfully created!")
        input("\nPress Enter to proceed...")

    def menu(self):
        system('clear')
        choice = '1'
        while choice != 'x':
            system('clear')
            print(text2art("Main Menu"))
            choice = input("""[1] -> Start race
[2] -> Check driver stats
[3] -> Enter the garage
[x] -> Exit the game

""")
            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.loading()
                self.driver.check_stats()
            elif choice == '3':
                self.enter_the_garage()
            if choice != 'x':
                input('\nPress Enter to proceed...')
            elif choice == 'x':
                self.exit_game()

    def loading(self) -> None: 
        system('clear')
        print(text2art("Loading"))
        for char in trange(100):
            time.sleep(0.01)
        time.sleep(2)
        system('clear')

    def start_game(self):
        self.music_player_event.clear()
        print('Hello world')
        time.sleep(3)
        self.music_player_event.set()

    def play_music(self):
        pygame.init()
        pygame.mixer.music.load(self.songs[0])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play()
        pygame.time.delay(372000)
        pygame.mixer.music.load(self.songs[1])
        pygame.mixer.music.play()
        self.music_player_event.wait()
        pygame.time.delay(203000)
        pygame.mixer.music.load(self.songs[2])
        pygame.mixer.music.play()
        pygame.time.delay(237000)
        pygame.mixer.music.load(self.songs[3])
        pygame.mixer.music.play()
        pygame.time.delay(243000)
        pygame.mixer.music.load(self.songs[4])
        pygame.mixer.music.play()
        pygame.time.delay(201000)
        pygame.mixer.music.load(self.songs[5])
        pygame.mixer.music.play()
        pygame.time.delay(216000)



    def enter_the_garage(self):
        self.loading()
        self.garage = Garage(self.driver.car_shop)
        self.garage.show_all_cars()
        input('\nPress Enter to proceed...')
        while True:
            system('clear')
            print(text2art("Garage"))
            choice = input('''What do you want to do here?
            
[1] - Buy the car
[2] - Sell the car
[3] - Back to menu

''')
            if choice == '1':
                system('clear')
                self.garage.car_shop.show_car_dict()
                name = input('Insert the name of desired car: ')
                model = input('Insert the model of desired car: ')
                price = self.garage.car_shop.car_buy(name, model, self.driver.money)
                self.driver.money = self.driver.money - price
            elif choice == '2':
                system('clear')
                self.garage.show_all_cars()
                name = input('Insert name of car which you want to sell: ')
                price = self.driver.car_shop.car_sell(name)
                self.driver.money = self.driver.money + price
            elif choice == '3':
                return 0
            

    def exit_game(self):
        system('clear')
        print(text2art('Thanks for playing!'))
        pygame.quit()
        exit(0)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    game = Game()