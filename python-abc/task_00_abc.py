#!/usr/bin/python3
from abc import ABC, abstractmethod
'''
Define the Abstract Base Class Animal
'''


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Bark'

class Cat(Animal):
    def sound(self):
        return 'Meow'
