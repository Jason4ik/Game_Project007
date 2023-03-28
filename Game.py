from os import system
import time
from CarShop import CarShop
from Car import Car

class Driver:
    def __init__(self, name: str, age: int, glasses: str, gloves: str, shoes: str):
        self.name = name
        self.age = age
        self.glasses = glasses
        self.gloves = gloves
        self.shoes = shoes
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
        print(f'\tAge: {self.age}')
        print(f'\tMoney: {self.__money}$')
        print(f'\tLevel: {self.__level}')
        print(f'\tXP: {self.__xp}')
        print(f'\tGlasses: {self.glasses}')
        print(f'\tGloves: {self.gloves}')
        print(f'\tShoes: {self.shoes}')
class Race:
    pass


if __name__ == "__main__":
    my_driver = Driver('Georg', 22, "Black", "Leather", 'Sneakers')
    my_driver.check_stats()