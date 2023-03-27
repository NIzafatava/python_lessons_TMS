# # 1
#
class Auto:

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        print(self.age + 1)


auto = Auto('kia', 12, 'kvs')
print(Auto.move(auto))
print(Auto.birthday(auto))



# 2


import time

class Auto:


    def move(self):
        print('move')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Truck(Auto):

    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        super().move()
        print('Attention, move')

class Car(Auto):

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'move, max speed is {self.max_speed}')


my_truck = Truck(4)
my_car = Car(12)
print(my_car.max_speed)
print(my_truck.max_load)
Auto.move(my_car)
my_car.move()
my_truck.move()


# 3
# import json
#
# class TelephoneBook:
#
#     def __init__(self, last_name=None, first_name=None, phone=None, info_telephone_book=None):
#         if info_telephone_book is None:
#             self.last_name = last_name
#             self.first_name = first_name
#             self.phone = phone
#         else:
#                 self.last_name, self.first_name, self.phone = str(info_telephone_book).replace(" ", '').split("|")
#
#     def input_contact_data(self):
#         self.last_name = input('Введите фамилию: ')
#         self.first_name = input('Введите имя: ')
#         self.phone = input('Введите номер телефона')
#
#     def result(self):
#         return print(f'{self.first_name},  {self.last_name}, {self.phone}')
#
#
# class Contacts(TelephoneBook):
#     def find_contact(self, contact_name):
#         with open('contacts.json') as json_file:
#             for line in json_file:
#                 contact = TelephoneBook(info_telephone_book=line)
#                 print(contact)
#                 if (contact.last_name) ==contact_name:
#                     return contact
#
#     # def add_contact(self):
#     #     new_contact = TelephoneBook()
#     #     new_contact.input_contact_data()
#     #     with open('contacts.json', 'a') as json_file:
#     #         json.dump(new_contact, json_file)
#     #         json_file.write()
#
#     # def delete_contact(self):
#
# my_contact = Contacts('Izofatova')
# # Contacts.add_contact(my_contact)
# print(Contacts.find_contact(Contacts, 'Izofatova'))
