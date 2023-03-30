# https://amankharwal.medium.com/130-python-projects-with-source-code-61f498591bb

# 1 Number Guessing Game

# import random
# bot = random.randint(1, 100)
# player = int(input('Введите число от 1 до 100: '))
# while bot != player:
#     if player < bot:
#         print('Число слишком мало')
#         player = int(input('Введите число от 1 до 100: '))
#     elif player > bot:
#         print('Число слишком велико')
#         player = int(input('Введите число от 1 до 100: '))
#     else:
#         break
# print('Вы угадали')

# 2 Group Anagrams   ???????

# from collections import defaultdict
#
# def group_anagrams(a):
#     dfdict = defaultdict(list)
#     for i in a:
#         sorted_i = " ".join(sorted(i))
#         dfdict[sorted_i].append(i)
#     return dfdict.values()
# words = ["tea", "eat", "bat", "ate", "arc", "car"]
# print(group_anagrams(words))


# 3 Find Missing Number

# def findmissnum(n):
#     numbers = set(n)
#     leng = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i  not in numbers:
#             output.append(i)
#     return output
#
# list_ = [1, 2, 5]
# print(findmissnum(list_))

#4 Print Emojis

    # pip install emoji
    # import emoji
    # print(emoji.emojize('Love: 	:couple_with_heart_person_person_light_skin_tone_medium-light_skin_tone:'))


#5 Reverse a String

# def reverse_string(string_):
#     return string_[::-1]
#
# words_ = 'Hellow world'
# print(reverse_string(words_))

#6 SequenceMatcher

# from difflib import SequenceMatcher
# text1 = "My Name is Aman Kharwal"
# text2 = "Hi, My Name is Aman Kharwal"
# sequenceScore = SequenceMatcher(None, text1, text2).ratio()
# print(sequenceScore)

# 7 Find Duplicate Values

# def dupl_values(x):
#     duplicates = []
#     length = len(x)
#     for i in range(length):
#         n = i + 1
#         for a in range(n, length):
#             if x[i] == x[a] and x[i] not in duplicates:
#                 duplicates.append(x[i])
#         return duplicates
#
# names = ["Aman", "Akanksha", "Divyansha", "Devyansh", "Aman", "Diksha", "Akanksha"]
# print(dupl_values(names))

#8 Age Calculator


# def ageCalculator(y, m, d):
#     import datetime
#     today = datetime.datetime.now().date()
#     dob = datetime.date(y, m, d)
#     age = int((today-dob).days / 365.25)
#     print(age)
# ageCalculator(2000, 9, 3)

#9 проверка на палиндром

# string = 'нежен'
#
# left_index = 0
# right_index = len(string) - 1
# while left_index != right_index:
#     left_index += 1
#     right_index -= 1
#     if string[left_index] != string[right_index]:
#         print(False)
# else:
#     print(True)


# 10. дан словарь, создать новый словарь, поменяв местами ключ и значение.

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# def change_dict(dict_: dict) -> dict:
#         dict2 = {}
#         for key in dict_:
#             print(dict_[key])
#             dict2[dict_[key]] = key
#         return dict2
#
#
# print(change_dict(dict_))

# 2 ой способ
#
# dict2 = {dict_[key]: key for key in dict_ }
# print(dict2)

# 11 написать с помощью рекурсии нахождение факториала
#
# def fact(n: int) -> int:
#     """
#     определяет факториал числа n
#     :param n:
#     :return:
#     """
#     if n < 0:
#         return
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(-2))
# print(fact.__doc__)


# 12. узнать версию питона

# import sys
# print(sys.version)

# 13. узнть текущее дата и время

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ", now)
# # print (now.strftime("%Y-%m-%d %H:%M:%S"))


# 14. декоратор на кэш

#
from functools import cache
from typing import Callable
from functools import wraps
#
# def create_cache(func: Callable) -> Callable:
#     cache_ = {}
#     @wraps(func)
#     def inner(*args):
#         if args in cache_:
#             return
#         result = func(*args)
#         cache_[args] = result
#         return func(*args)
#     return inner
#
# @cache
# def add(a: int,b: int) -> int:
#     print('выполняем тело функции add')
#     return a + b
#
# print(add(2, 3))
# print(add(2, 3))
# print(add(5, 3))


# def cache_func(func: Callable) -> Callable:
#     cache_ = {}
#     @wraps(func)
#     def inner(*args, **kwargs):
#         cache_items = args + tuple(kwargs.items())
#         if cache_items in cache_:
#             return
#         cache_[cache_items] = func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return inner
#
# @cache
# def add(a: int,b: int) -> int:
#     print('выполняем тело функции add')
#     return a + b
#
# print(add(2, 3))
# print(add(2, 3))
# print(add(5, 3))



# 15. To DO LIST

from dataclasses import dataclass
# from enum import Enum
# class PriorityEnum(Enum):
#     LOW = 'low'
#     HIGH_ = 'high'
#     MEDIUM = 'medium'
#
# my_priority = PriorityEnum.HIGH_
# my_priority2 = PriorityEnum.HIGH
# print(my_priority == my_priority2)


# Реализовать To Do список используя классы.
# В задаче хранить описание и приоритет (high, medium, low, по умолчанию low).
# Методы класса ToDoList:
# - добавить задачу
# - изменить описание задачи
# - изменить приоритет задачи
# - удалить задачу
# - вернуть список задач, отсортированный по приоритету (сначала высокий)
# - сохранить список в файл/загрузить из файла

# from enum import Enum, IntEnum
# import csv
#
# class PriorityEnum(IntEnum):
#     LOW = 0
#     MEDIUM = 1
#     HIGH = 2
#
#
# class Task:
#     def __int__(self, task_name: str, task_discr: str, priority: PriorityEnum):
#         self.task_name = task_name
#         self.task_discr = task_discr
#         self.priority = priority
#
#     def __repr__(self):
#         return f'{self.task_name}, {self.task_discr}, {self.priority}'
#
#
# class ToDoList:
#     def __init__(self):
#         self.to_do_list: list[Task] = []
#
#     def add_task(self, task: Task):
#         self.to_do_list.append(task)
#
#     def change_task(self, task: Task, new_task: str):
#         if task in self.to_do_list:
#             self.to_do_list[self.to_do_list.index(task)].task = new_task
#
#     def change_priority(self, task: Task, new_priority: PriorityEnum):
#         if task in self.to_do_list:
#             self.to_do_list[self.to_do_list.index(task)].priority = new_priority
#
#     def del_task(self, task: Task):
#         if task in self.to_do_list:
#             self.to_do_list.remove(task)
#
#     def sort_task(self) -> list[Task]:
#         return sorted(self.to_do_list, key = lambda task: task.priority, reverse=True)
#
#     def save_file(self):
#         file_name = 'task.csv'
#         with open (file_name, 'w', encoding = utf -8) as file:
#             writer = csv.writer(file)
#             writer.writerow(['name', 'task', 'priority'])
#             result = [[element.task_name, element.task_discr, element.priority] for element in self.to_do_list]
#             writer.writerows(result)
#
#
# task = Task('')
# # task2 = Task('first2', 'first task', PriorityEnum.MEDIUM)
# # task3 = Task('first3', 'first task', PriorityEnum.HIGH)
# # task4 = Task('first4', 'first task', PriorityEnum.LOW)
#
# to_do_list = ToDoList()
# to_do_list.sort_task()
# to_do_list.sort_task(task)
# to_do_list.sort_task(task2)
# to_do_list.sort_task(task3)
# to_do_list.sort_task(task4)
#
# print(to_do_list.sort_task())
# print(to_do_list.to_do_list)
#
# to_do_list.change_task(task3, 'edit task')
# print(to_do_list.sort_task())
#
# to_do_list.del_task(task4)
# print(to_do_list.sort_task())
#
# to_do_list.change_priority(task, PrioritetEnum.HIGH)
# print(to_do_list.sort_task())


# to_do_list.save_file()



# 16. Задание по теме "Классы и объекты"
# Задача 1
# Создайте класс Soda (для определения типа газированной воды),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки,
# а иначе отобразится следующая фраза: Обычная газировка.
# Решение

# class Soda:
#     def __init__(self, addition = None):
#         self.addition = addition
#
#     def show_my_drink(self):
#         if self.addition is not None:
#             print(f'Soda and {self.addition}')
#         else:
#             print('Soda')
#
# my_soda = Soda('sigar')
# my_soda.show_my_drink()


# 17.Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.


class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'



# 18. Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она реализовала методы
# set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг.
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов.


# class KgToPounds:
#     def __init__(self, kg):
#         self._kg = kg
#
#     def to_pounds(self):
#         return f' pounds = {self._kg/2}'
#
#     @property
#     def kg(self):
#         return self._kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self._kg = new_kg
#         else:
#             raise ValueError('Килограммы задаются только числами')
#
# my_pounds = KgToPounds(10)
# print(my_pounds.to_pounds())
# my_pounds.kg = 12
# print(my_pounds.kg)

# 19.





