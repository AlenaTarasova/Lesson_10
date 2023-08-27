"""Возьмите 1-3 любые задания из прошлых семинаров, которые вы уже решали. Превратите
функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра."""

import math


class QuadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def equation_roots(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        if self.a != 0:
            if discr > 0:
                x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
                x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
                return f"x1 = {x1:.3f} \nx2 = {x2:.3f}"
            elif discr == 0:
                x = -self.b / (2 * self.a)
                return f"x1 = x2 = {x:.3f}"
            else:
                return "Корней нет"

        else:
            return "Уравнение не является квадратным"


quadratic = QuadraticEquation(2, 5, -3)
print(quadratic.equation_roots())