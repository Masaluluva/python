# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:

    def __init__(self, name,color,type):
        self.name = name
        self.color = color
        self.type = type
    def purchase(self):
        print("Материал закуплен")
    def make(self):
        print("Игрушка изготовлена")
    def make_color(self):
        print("Игрушка покрашена")

class AnimalToy(Toy):
     pass

class CartoonToy(Toy):
     pass

class Fabrika():

    def our_type(self,type):
        if type == "animal":
            return AnimalToy
        elif type == "cartoon":
            return CartoonToy

animal_toy = Toy("Cat", "black", "animal")
cartoon = CartoonToy("Doll", "white", "cartoon")

animal_toy.purchase()
animal_toy.make()
animal_toy.make_color()

fabrika = Fabrika()
cls = fabrika.our_type("animal")
print(cls)





