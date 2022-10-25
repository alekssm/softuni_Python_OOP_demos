class Animal:
    _sound = "Nice"

    def __init__(self, species):
        self.species = species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = "Meow"

    def __init__(self, species):
        super().__init__(species)


class Dog(Animal):
    _sound = "Woof-woof"

    def __init__(self, species):
        super().__init__(species)


class Chicken(Animal):
    _sound = "Chick"

    def __init__(self, species):
        super().__init__(species)


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)


animals = [Cat('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)