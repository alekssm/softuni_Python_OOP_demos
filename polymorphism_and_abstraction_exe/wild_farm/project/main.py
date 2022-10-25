from pythonProject.python_oop_course.polymorphism_and_abstraction.polymorphism_and_abstraction_exe.wild_farm.project.animals.birds import \
    Owl, Hen
from pythonProject.python_oop_course.polymorphism_and_abstraction.polymorphism_and_abstraction_exe.wild_farm.project.food import \
    Meat, Vegetable, Fruit

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)