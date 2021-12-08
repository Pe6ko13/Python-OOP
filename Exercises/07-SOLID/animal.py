from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bau'


class Chicken(Animal):
    def make_sound(self):
        return 'ko ko'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())
        # if animal.species == 'cat':
        #     print('meow')
        # elif animal.species == 'dog':
        #     print('woof-woof')


animals = [Cat('cat'), Dog('dog'), Chicken('chick')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
