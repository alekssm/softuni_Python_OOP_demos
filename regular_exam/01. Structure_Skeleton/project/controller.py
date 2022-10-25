from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race



class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if model == car.model:
                raise Exception(f"Car {model} is already created!")

        if car_type == MuscleCar.__name__:
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."
        if car_type == SportsCar.__name__:
            car = SportsCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver_name == driver.name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race_name == race.name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not any(x.name == driver_name for x in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")

        for driver in self.drivers:
            if driver_name == driver.name:

                suitable_cars = self.find_suitable_cars(car_type)
                if len(suitable_cars) == 0:
                    raise Exception(f"Car {car_type} could not be found!")

                new_car = suitable_cars[-1]
                if driver.car is None:
                    driver.car = new_car
                    new_car.is_taken = True
                    return f"Driver {driver_name} chose the car {new_car.model}."
                else:
                    old_car = driver.car
                    driver.car = new_car
                    new_car.is_taken = True
                    old_car.is_taken = False
                    return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not any(x.name == race_name for x in self.races):
            raise Exception(f"Race {race_name} could not be found!")
        if not any(x.name == driver_name for x in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")

        for driver in self.drivers:
            if driver_name == driver.name:
                if driver.car is None:
                    raise Exception(f"Driver {driver_name} could not participate in the race!")

                for race in self.races:
                    if race_name == race.name:
                        if driver in race.drivers:
                            return f"Driver {driver_name} is already added in {race_name} race."
                        race.drivers.append(driver)
                        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not any(x.name == race_name for x in self.races):
            raise Exception(f"Race {race_name} could not be found!")

        for race in self.races:
            if race_name == race.name:
                if len(race.drivers) < 3:
                    raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
                else:
                    result = sorted([x for x in race.drivers], key=lambda x: x.car.speed_limit, reverse=True)[0:3]
                    print_result = ""
                    for driver in result:
                        driver.number_of_wins += 1
                        print_result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}."
                        print_result += "\n"
                    return print_result

    def find_suitable_cars(self, car_type):
        result = [x for x in self.cars if x.__class__.__name__ == car_type and not x.is_taken]
        return result
