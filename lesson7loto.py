# Лото

import random
import sys

barrels = random.sample(range(90), 90)
game_num = random.sample(range(90), 30)
player = 15
comp = 15
player_num = random.sample(game_num, 15)
comp_num = [i for i in game_num if not i in player_num]
player_card = [player_num [:5], player_num [5:10], player_num [10:]]
comp_card = [comp_num[:5], comp_num[5:10], comp_num[10:]]

for p1ayerl in player_card:
    p1ayerl.sort()
    p1ayerl.insert(random.randint(0, 4), ' ')
    p1ayerl.insert(random.randint(0, 5), ' ')
    p1ayerl.insert(random.randint(0, 6), ' ')
    p1ayerl.insert(random.randint(0, 9), ' ')

for compl in comp_card:
    compl.sort()
    compl.insert(random.randint(0, 4), ' ')
    compl.insert(random.randint(0, 5), ' ')
    compl.insert(random.randint(0, 6), ' ')
    compl.insert(random.randint(0, 9), ' ')

def body(s):
    if s == 0:
        print('{:-^27}'.format('Карта игрока '))
        for line1 in player_card:
            for player in line1:
                print('{0:>2}'.format(player), end=' ')
            print()
        print('{:-^27}\n'.format('-'))
    if s == 1:
        print('{:-^27}'.format(' Карта компьютера '))
        for line2 in comp_card:
            for comp in line2:
                print('{0:>2}'.format(comp), end=' ')
            print()
        print('{:-^27}\n'.format('-'))

def rate_player ():
    a = input('Такая цифра есть? (+/-): ')
    if a == '+':
        if barrel in player_num:
            for q in player_card:
                try:
                  q.insert(q.index(barrel), 'Х')
                  q.pop(q.index(barrel))
                except ValueError:
                    continue
            print('\n')
            return 1
        else:
            print('\nИгра окончена')
            sys.exit()
    if a == '-':
        if barrel in player_num:
            print('\nИгра окончена')
            sys.exit()
        else:
            print('\n')

def rate_comp():
    if barrel in comp_num:
        for z in comp_card:
            try:
                z.insert(z.index(barrel), 'Х')
                z.pop(z.index(barrel))
            except ValueError:
                continue
        return 1

allbarrels = 90
for barrel in barrels:
    allbarrels -= 1
    print('\nБочонок №: {} (В игре осталось: {} бочонков)\n'.format(barrel, allbarrels))
    body(0) or  body(1)
    if rate_player() == 1:
        player -= 1
    if rate_comp() == 1:
        comp -= 1
    if allbarrels == 0:
        print('\n Игра окончена!')
        sys.exit()
    if comp == 0:
        print('\n Вы проиграли!')
        sys.exit()
    if player == 0:
        print('\n Вы выиграли!!!')
        sys.exit()