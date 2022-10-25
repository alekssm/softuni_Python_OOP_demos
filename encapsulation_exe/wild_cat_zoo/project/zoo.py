from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def __enough_budget(self, price):
        return self.budget >= price

    def __get_all_salaries(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        return salaries

    def __get_animal_care_cost(self):
        cost = sum([x.money_for_care for x in self.animals])
        return cost

    def add_animal(self, animal, price):
        if len(self.animals) == self.animal_capacity:
            return "Not enough space for animal"
        if not self.__enough_budget(price):
            return "Not enough budget"
        self.animals.append(animal)
        self.budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if not self.__enough_budget(self.__get_all_salaries()):
            return "You have no budget to pay your workers. They are unhappy"
        self.budget -= self.__get_all_salaries()
        return f"You payed your workers. They are happy. Budget left: {self.budget}"

    def tend_animals(self):
        if not self.__enough_budget(self.__get_animal_care_cost()):
            return "You have no budget to tend the animals. They are unhappy."
        self.budget -= sum([x.money_for_care for x in self.animals])
        return f"You tended all the animals. They are happy. Budget left: {self.budget}"

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        cheetahs = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals"
        result += "\n"
        result += f"----- {len(lions)} Lions:"
        for lion in lions:
            result += "\n"
            result += f"{str(lion)}"
        result += "\n"
        result += f"----- {len(tigers)} Tigers:"
        for tiger in tigers:
            result += "\n"
            result += f"{str(tiger)}"
        result += "\n"
        result += f"----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            result += "\n"
            result += f"{str(cheetah)}"
        return result

    def workers_status(self):
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers"
        result += "\n"
        result += f"----- {len(keepers)} Keepers:"
        for keeper in keepers:
            result += "\n"
            result += f"{str(keeper)}"
        result += "\n"
        result += f"----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result += "\n"
            result += f"{str(caretaker)}"
        result += "\n"
        result += f"----- {len(vets)} Vets:"
        for vet in vets:
            result += "\n"
            result += f"{str(vet)}"
        return result

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
