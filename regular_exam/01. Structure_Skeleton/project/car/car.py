from abc import ABC, abstractmethod


class Car(ABC):
    MIN_MODEL_SYMBOLS = 4
    MAX_SPEED_LIMIT = 1
    MIN_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @classmethod
    def __validate_model(cls, value):
        if len(value) < cls.MIN_MODEL_SYMBOLS:
            raise ValueError(f"Model {value} is less than 4 symbols!")

    @classmethod
    def __validate_speed_limit(cls, value):
        if value < cls.MIN_SPEED_LIMIT or value > cls.MAX_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {cls.MIN_SPEED_LIMIT} and {cls.MAX_SPEED_LIMIT}!")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__validate_model(value)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value
