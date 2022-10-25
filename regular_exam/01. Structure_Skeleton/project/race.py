from project.driver import Driver
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
