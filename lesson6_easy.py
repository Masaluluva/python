# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Car:
    def __init__(self,name,car_speed,car_color, is_police):
        self.name = name
        self.car_speed = car_speed
        self.car_color = car_color
        self.is_police = bool(is_police)
    def go(self):
        if self.car_speed !=0:
            print("Maшина " + self.name +  " поехала!")
    def stop(self):
        if self.car_speed == 0:
            print("Maшина " + self.name +  " остановилась!")
    def turn_direction(self,side):
        if side == 1:
            print("Maшина " + self.name +  " повернула направо!")
        if side == 2:
            print("Maшина " + self.name +  " повернула налево!")


TownCar = Car('Renault',80,"white"," ")
SportCar = Car("Ferrari",150,"red"," ")
WorkCar = Car("Hyndai",0,"Grey"," ")
PoliceCar = Car("Kia",150,"blue", "...")

print(TownCar.car_color,TownCar.car_speed)
print(SportCar.name)
PoliceCar.go()

class SuperCar(Car):
    def fly(self):
        print("Cупер машина взлетает!")

new_car = SuperCar('Polet', 200, "metallik"," ")
print(new_car.name)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

