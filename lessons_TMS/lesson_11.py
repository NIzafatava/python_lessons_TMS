# import json

#
# class Contact:
#     def __init__(self, name: str, phone: str) -> None:
#         self.name = name
#         self.phone = phone
#
#     # def __str__(self):
#     #     return f"{self.name}: {self.phone}"
#
#     def __repr__(self):
#         # return f'{self.name}: {self.phone}'
#         return f'Contact({self.name}: {self.phone})'


from dataclasses import dataclass
from datetime import date
# @dataclass
# class Contact:
#     name: str
#     phone: str
#
# contact = Contact('Nastya', '429469')
# print(f'{contact.name=}:{contact.phone=}')


#classmethod

# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name}: {self.age}'
# my_user = User('Nastya', 25)
# print(my_user.name)
# print(my_user)

#
# @dataclass
# class User:
#     name: str
#     age: int
#
#     @classmethod
#     def from_year(cls, name: str, year: int) -> "User":
#         current_year = date.today().year
#         age = current_year - year
#         return cls(name, age)
#
#
#     # def __str__(self):
#     #     return f'{self.name}: {self.age}'
# my_user = User('Nastya', 25)
# print(my_user.name)
# print(my_user)
# my_user2 = User.from_year('Sasha', 1990)
# print(my_user2)
#
# #Staticmethod
#
#
# @dataclass
# class User:
#     name: str
#     age: int
#
#     @staticmethod
#     def say_hi() -> None:
#         print('Hello World')
#
#
#
#     # def __str__(self):
#     #     return f'{self.name}: {self.age}'
# my_user = User('Nastya', 25)
# my_user.say_hi()
# User.say_hi()
#
#
# #property
# @dataclass
# class Contact:
#     name: str
#     code: int
#     phone: int
#
#     @property
#     def full_phone_number(self):
#         return f"+{self.code}{self.phone}"
#
# contact = Contact('Nastya', 375, 72740)
# print(contact.full_phone_number)
#
#
# @dataclass
# class BankAccount:
#     balance_usd: int
#
#     @property
#     def balance_euro(self):
#         return 1.2 * self.balance_usd
#
#
#
#     @balance_euro.setter
#     def balance_euro(self, value_euro):
#         self.balance_usd = value_euro / 1.2


# class BankAccount:
#     def __init__(self):
#         self._balance_usd = 0
#
#     @property
#     def balance_euro(self):
#         return 1.2 * self._balance_usd
#
#     @balance_euro.setter
#     def balance_euro(self, value_euro):
#         self._balance_usd = value_euro / 1.2
#
#     @property
#     def balance_blr(self):
#         return self._balance_usd * 2.7
#
#     @balance_blr.setter
#     def balance_blr(self, value_blr):
#         self._balance_usd = value_blr / 2.7
#
#
# account = BankAccount()
# # print(account.balance_usd)
# print(account.balance_euro)
# account.balance_euro = 100
# print(account.balance_euro)
# print(account.balance_blr)
# account.balance_blr = 200
# print(account.balance_euro)
# print(account.balance_blr)


# To Do List