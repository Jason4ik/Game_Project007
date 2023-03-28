from os import system
import time
from CarShop import CarShop
from Car import Car

class Driver:
    def __init__(self, name, age, glasses, gloves, shoes):
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


class Race:
    pass