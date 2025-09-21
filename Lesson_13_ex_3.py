print("Lesson 13. Home task №3.")
"""
Паттерн «Стратегия»
• Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
• Создайте несколько классов, каждый реализует определенную
стратегию математической операции, например, Addition,
Subtraction, Multiplication, Division. Каждый класс должен
содержать метод execute, который принимает два числа и
выполняет соответствующую операцию.
• Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate, который
выполняет операцию с помощью текущей стратегии.
"""

from abc import ABC, abstractmethod


class Action():
    @abstractmethod
    def execute(self, x, y):
        pass


# Стратегия сложения Addition
class action_addition(Action):
    def execute(self, x, y):
        return x + y
# Стратегия вычитания Subtraction
class action_subtraction(Action):
    def execute(self, x, y):
        return x - y

# Стратегия умножения Multiplication
class action_multiplication(Action):
    def execute(self, x, y):
        return x * y

# Стратегия умножения Division
class action_division(Action):
    def execute(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ZeroDivisionError('Деление на ноль')

#_______________________________________________________
class Calculator:
    def __init__(self):
        self.action = None

    def set_strategy(self, action):
        self.action = action

    def calculate(self, x, y):
        return self.action.execute(x, y)

#_______________________________________________________
calc_add = Calculator()
calc_sub = Calculator()
calc_mul = Calculator()
calc_div = Calculator()
#_______________________________________________________
calc_add.set_strategy(action_addition())
calc_sub.set_strategy(action_subtraction())
calc_mul.set_strategy(action_multiplication())
calc_div.set_strategy(action_division())
#_______________________________________________________
while True:
    x = int(input('Enter x:'))
    y = int(input('Enter y: '))
    result_add = calc_add.calculate(x, y)
    result_sub = calc_sub.calculate(x, y)
    result_mul = calc_mul.calculate(x, y)
    result_div = calc_div.calculate(x, y)
    print(result_add)
    print(result_sub)
    print(result_mul)
    print(result_div)
#_______________________________________________________