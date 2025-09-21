print("Lesson 13. Home task №2.")
"""
 Паттерн «Фабричный метод»
• Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
• Создайте классы Dog и Cat, которые наследуют от Animal и
реализуют метод speak.
• Создайте класс AnimalFactory, который использует паттерн
«Фабричный метод» для создания экземпляра Animal. Этот
класс должен иметь метод create_animal, который принимает
строку («dog» или «cat») и возвращает соответствующий
объект (Dog или Cat)
"""

#Cоздайте абстрактный класс Animal, у которого есть абстрактный метод speak.
from abc import ABC, abstractmethod
class Animal():
    @abstractmethod
    def speak(self):
        pass

#Создайте классы Dog и Cat, которые наследуют от Animal и реализуют метод speak
class Dog(Animal):
    def speak(self):
        print("гав!")
        return "Собака создана"

class Cat(Animal):
    def speak(self):
        print("мяу!")
        return "Кошка создана"


# #Создайте класс AnimalFactory, который использует паттерн
# «Фабричный метод» для создания экземпляра Animal. Этот
# класс должен иметь метод create_animal, который принимает
# строку («dog» или «cat») и возвращает соответствующий
# объект (Dog или Cat)
class AnimalFactory:
    @staticmethod
    def create_animal(type_of_animal):
        if type_of_animal == "dog":
            return Dog()
        elif type_of_animal == "cat":
            return Cat()
        else:
            raise ValueError ("Не известное животное")
#______________________________________

factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
cat2 = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())
print(cat2.speak())
