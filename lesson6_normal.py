import random
#Задача - 1
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, armor, damage, health): # имя, броня, урон, жизнь
        self.health = health
        self.name = str(name)
        self.armor = armor
        self.damage = damage

    def _number_damage(self, damage):
        self.health -= damage
        print('{}: {} жизни'.format(self.__class__.__name__, round(self.health,1)))


    def attack(self, player):
        damage = self.damage / player.armor
        player._number_damage(damage)


class Player(Person):
    pass


class Enemy(Person):
    pass

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        while True:
             if self.player.health <= 0:
                print('Победил {}, жизни {}'.format(self.player.name, round(self.player.health,1)))
                break
             elif self.enemy.health <= 0:
                print('Победил {}, жизни {}'.format(self.enemy.name, round(self.enemy.health,1)))
                break

             self.enemy.attack(self.player)
             self.player.attack(self.enemy)



enemy = Enemy("Vangog", 50, 40, 50)
player = Player("Pearl", 50, 45, 50)

game_1 = Game(player, enemy)
game_1.start()

