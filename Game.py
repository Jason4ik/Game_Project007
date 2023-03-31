from os import system
import time
from CarShop import CarShop
from Car import Car
from CarRace import CarRace
import pygame
from art import *
from tqdm import trange
import threading

class Driver:
    def __init__(self, name: str, gender:str, age: int, glasses: str, gloves: str, shoes: str):
        self.name = name
        self.age = age
        self.glasses = glasses
        self.gloves = gloves
        self.shoes = shoes
        self.gender = gender
        self.car_shop = CarShop()
        self.tuned_cars = []
        self.races = 0
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
        if self.__xp >= 1000:
            self.__level += 1
            self.__xp = self.__xp - 1000

    def check_stats(self):
        system('clear')
        print(f"Driver {self.name}".center(50, '='))
        print("Stats:")
        print(f'\tAge:        {self.age}')
        print(f'\tMoney:      {self.__money}$')
        print(f'\tLevel:      {self.__level}')
        print(f'\tXP:         {self.__xp}')
        print(f'\tRaces done: {self.races}')
        print(f'\tGlasses:    {self.glasses}')
        print(f'\tGloves:     {self.gloves}')
        print(f'\tShoes:      {self.shoes}')
        print("Cars:")
        self.car_shop.garage_list()
        print('Tuned cars:')
        for car in self.tuned_cars:
            car.get_info()
class Game:
    _instance = None
    def __init__(self):
        self.loading()
        self.driver = None
        self.songs = ['./Music/Riders-on-the-Storm.mp3', './Music/Skinnyman-Static-X.mp3', './Music/Chingy - I Do.mp3', './Music/Christopher Lawrence - Rush Hour.mp3', './Music/Goldfrapp - Ride A White Horse.mp3','./Music/Need For Speed Carbon Soundtrack - Hard Drivers.mp3']
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
        time.sleep(1)
        system('clear')

    def start_game(self):
        self.race = CarRace()
        self.race.Start_Game()
        print('Choose the car to race: ')
        self.driver.car_shop.garage_list()
        car_name = input('Insert the name of car: ')
        self.race.go()
        pygame.mixer.quit()

        result = self.race.exp(self.driver.car_shop.garage[car_name]['pic'], self.driver.car_shop.garage[car_name]["acceleration"])
        self.music_player = threading.Thread(target=self.play_music)
        self.music_player.start()
        self.driver.races += 1
        if result == 1:
            self.driver.money = self.driver.money + 10000
            self.driver.level = 1000
        elif result == 0:
            self.driver.money = self.driver.money + 1000
            self.driver.level = 100


    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.songs[0])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play()
        pygame.time.delay(372000)
        pygame.mixer.music.load(self.songs[1])
        pygame.mixer.music.play()
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
        while True:
            system('clear')
            print(text2art("Garage"))
            choice = input('''What do you want to do here?
            
[1] - Buy the car
[2] - Sell the car
[3] - Show my cars
[4] - Tuning
[x] - Back to menu

''')
            if choice == '1':
                system('clear')
                self.driver.car_shop.show_all_cars()
                name = input('Insert the name of desired car: ')
                car = Car(car_name=name)
                system('clear')
                car.get_info()
                choice = input("Youy sure you want to buy this car?[y/n]")
                if choice.lower() == 'y':
                    price = self.driver.car_shop.car_buy(name, self.driver.money)
                    self.driver.money = self.driver.money - price
                elif choice.lower() == 'n':
                    continue
            elif choice == '2':
                system('clear')
                self.driver.car_shop.garage_list()
                name = input('Insert name of car which you want to sell: ')
                price = self.driver.car_shop.car_sell(name)
                self.driver.money = self.driver.money + price
            elif choice == '3':
                self.driver.car_shop.garage_list()
                print('Tuned cars:')
                for car in self.driver.tuned_cars:
                    car.get_info()
            elif choice == '4':
                self.driver.car_shop.garage_list()
                car_choice = input('Choose the car for tunning: ')
                car = Car(car_choice)
                self.driver.tuned_cars.append(car)
                upgrades = ["engine", 'suspencion', 'Red']
                print("Available upgrades:")
                print('\t\tEngine - upgrade heart of your car')
                print('\t\tSuspension - control your car as a God')
                print('\t\tChange color - respray your car in one of available colors[Red/Orange/Yellow/Green/Blue/Indigo/Violet/Coral]')

                upgr_choice = input('Choose your upgrades and write it with coma as a separator: ')
                self.driver.tuned_cars[self.driver.tuned_cars.index(car)].tuning(upgr_choice.split(','))
                print()
                car.get_info()
            if choice == 'x':
                return 0
            elif choice != 'x':
                input("Press Enter to proceed...")
            

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