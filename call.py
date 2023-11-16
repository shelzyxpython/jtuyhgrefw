# # WS 15.11.23
from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any
#
# class Thing:
#     def __init__(self, name, weight, price=0, dims=[]):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f'{self.__dict__}'
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float
#     dims: list = field(default_factory=list)
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#
# th = Thing('name', '15', 15000)
# th.dims.append(10)
# print(th)
# th2 = Thing('nbfds', 45, 12)
# print(th2)
# td = ThingData('name2', 12, 2.5)
# print(td)
# td2 = ThingData('name2', 121, 2.5)
# print(td == td2)


# class Vector3D:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (x**2 + y**2 + z**2) ** 0.5
#
# @dataclass
# class VectorData:
#     x: int
#     y: int
#     z: int
#     length: float = field(init=False)
#     pi: float = field(init=False)
#
#     def __post_init__(self):
#         self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#
#
# v = Vector3D(1, 2, 3)
# print(v.__dict__)


# @dataclass
# class Goods:
#     current_uid = 0
#
#     uid: int = field(init=False)
#     price: Any
#     weight: Any
#
#     def __post_init__(self):
#         print('Goods')
#         Goods.current_uid += 1
#         self.uid = Goods.current_uid
#
#
# class GoodMeassureFactory:
#
#     @staticmethod
#     def get_init_meassure():
#         return [0, 0, 0]
#
#
# @dataclass
# class Book(Goods):
#     title: str
#     author: str
#     price: int
#     weight: float
#     meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print('Book')
#
#
# g = Goods(1200, 2.5)
# print(g)
# g1 = Goods(1200, 2.5)
# print(g1)
# b = Book(2000, 2.5, 'gfds', 'fds')
# b.meassure[1] = 124
# print(b)


# class Car:
#
#     def __init__(self, model, max_speed, price):
#         self.model = model
#         self.max_speed = max_speed
#         self.price = price
#
#     def get_max_speed(self):
#         return self.max_speed
#
#
# @dataclass
# class CarD:
#     model: str
#     max_speed: int | float
#     price: int = field(default=0)
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_price(self):
#         return self.price
#
#
# CarData = make_dataclass('CarData',[('model', str), 'max_speed',('price', int, field(default=0))],
#                          namespace={'get_max_speed': lambda self: self.max_speed})
#
# cd = CarData('Lada Granta', 120, 6000000)
# print(cd.get_max_speed())
# print(cd.get_price())



## ЛАБОРАТОРНАЯ

# class Book:
#     def __init__(self, title, author, publisher):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#
#     def get_title(self):
#         return self.title
#
#     def set_title(self, title):
#         self.title = title
#
#     def get_author(self):
#         return self.author
#
#     def set_author(self, author):
#         self.author = author
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def __str__(self):
#         return f"Book title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}"
#
#
# book = Book('Пёс по имени Мани', 'Без понятия автора', 'Без понятия')
# print(book)


# class Pet:
#     def __init__(self, name, animial_type, age):
#         self.name = name
#         self.animal_type = animial_type
#         self.age = age
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_animal_type(self, animal_type):
#         self.animal_type = animal_type
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_animal_type(self):
#         return self.animal_type
#
#     def get_age(self):
#         return self.age
#
#     def __str__(self):
#         return f'Name:{self.name}\nAnimal type: {self.animal_type}\nAge:{self.age}'
#
#
# pet = Pet('Pesik', 'Dog', '13')
# print(pet)


# class Info:
#     def __init__(self, name, adress, age, phone_num):
#         self.name = name
#         self.adress = adress
#         self.age = age
#         self.phone_num = phone_num
#
#     def get_name(self):
#         return self.name
#
#     def get_adress(self):
#         return self.adress
#
#     def get_age(self):
#         return self.age
#
#     def get_phone_num(self):
#         return self.phone_num
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def set_adress(self, new_adress):
#         self.adress = new_adress
#
#     def set_age(self, new_age):
#         self.age = new_age
#
#     def new_phone_num(self, new_phone_num):
#         self.phone_num = new_phone_num
#
#
#
# info = Info("Ваше имя", "Ваш адрес", "Ваш возраст", "Ваш номер телефона")
# ppl_1 = Info("Имя 1", "Адрес 1", "Возраст 1", "Номер телефона 1")
# ppl_2 = Info("Имя 2", "Адрес 2", "Возраст 2", "Номер телефона 2")
# print(info)
# print(ppl_1)
# print(ppl_2)


