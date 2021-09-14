from abc import ABCMeta, abstractmethod

# Abstract Class
class Animal(metaclass=ABCMeta):
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))

    @abstractmethod
    def get_favourite_food(self):
        pass


class Dogs(Animal):
    def __init__(self, name) -> None:
        self.name = name

    def get_favourite_food(self):
        return "ribs"


d = Dogs("SDad")
d.hungry()
