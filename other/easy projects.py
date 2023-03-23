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


def cache_func(func: Callable) -> Callable:
    cache_ = {}
    @wraps(func)
    def inner(*args, **kwargs):
        cache_items = args + tuple(kwargs.items())
        if cache_items in cache_:
            return
        cache_[cache_items] = func(*args, **kwargs)
        return func(*args, **kwargs)
    return inner

@cache
def add(a: int,b: int) -> int:
    print('выполняем тело функции add')
    return a + b

print(add(2, 3))
print(add(2, 3))
print(add(5, 3))



