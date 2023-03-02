import math
import random



# Напишите программу, которая выводит на экран приветствие.
def test_greeting():

    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."


# Напишите программу, которая берет длину и ширину прямоугольника и считает его периметр и площадь.

def test_rectangle():

    a = 10
    b= 20

    perimeter = (a + b) * 2
    assert perimeter == 60

# Сосчитайте площадь
    area = a * b
    assert area == 200

# Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
# Используйте константу PI.

def test_circle():
    r = 23
    area = math.pi * (r ** 2)
    assert area == 1661.9025137490005

    length = 2 * math.pi * r
    assert length == 144.51326206513048

# Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.

def test_random_list():

    from random import randint

    l = [randint(1, 100) for i in range(10)]

    assert len(l) == 10
    assert l[0] < l[-1]


 # удалите из списка все пвтроряющиеся элементы

def test_unique_elements():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = set(l)
    l = list(l)

    assert isinstance(l, list )
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5












