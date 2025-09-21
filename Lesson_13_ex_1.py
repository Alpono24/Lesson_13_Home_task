print("Lesson 13. Home task №1.")
"""
Паттерн «Строитель»

• Создайте класс Pizza, который содержит следующие атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon.

• Создайте класс PizzaBuilder, который использует паттерн «Строитель» для создания экземпляра Pizza. 
Этот класс должен содержать методы для добавления каждого из атрибутов Pizza.

• Создайте класс PizzaDirector, который принимает экземпляр PizzaBuilder и содержит метод make_pizza, который использует PizzaBuilder для создания Pizza
"""

from dataclasses import dataclass

# 1. Создайте класс Pizza, который содержит следующие атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon
# class Pizza:
#     size: float = None
#     cheese: bool = False
#     pepperoni: bool = False
#     mushrooms: bool = False
#     onions: bool = False
#     bacon: bool = False

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def add_size(self, size):
        # print('Установить размер пиццы:')
        self.size = size

    def add_cheese(self):
        self.cheese = True

    def add_pepperoni(self):
        self.pepperoni = True

    def add_mushrooms(self):
        self.mushrooms = True

    def add_onions(self):
        self.onions = True

    def add_bacon(self):
        self.bacon = True

    def info(self):
        ingredients = []
        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.mushrooms:
            ingredients.append("mushrooms")
        if self.onions:
            ingredients.append("onions")
        if self.bacon:
            ingredients.append("bacon")
        print(f"Pizza size and ingredients: {self.size}, {', '.join(ingredients)}")


#2 Создайте класс PizzaBuilder, который использует паттерн «Строитель» для создания экземпляра Pizza.
#  Этот класс должен содержать методы для добавления каждого из атрибутов Pizza.

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_size(self, size):
        self.pizza.add_size(size)
        return self

    def add_cheese(self):
        self.pizza.add_cheese()
        return self

    def add_pepperoni(self):
        self.pizza.add_pepperoni()
        return self

    def add_mushrooms(self):
        self.pizza.add_mushrooms()
        return self

    def add_onions(self):
        self.pizza.add_onions()
        return self

    def add_bacon(self):
        self.pizza.add_bacon()
        return self

    def build(self):
        return self.pizza

# 3 Создайте класс PizzaDirector, который принимает экземпляр PizzaBuilder
# и содержит метод make_pizza, который использует PizzaBuilder для создания Pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        pizza = (self.builder.add_size('large').add_cheese().add_pepperoni().add_mushrooms().add_onions().build())
        return pizza


builder = PizzaBuilder()
director = PizzaDirector(builder)
my_pizza = director.make_pizza()
my_pizza.info()