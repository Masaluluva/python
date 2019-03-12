# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Созданы директории")
try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Директории удалены")

# Задача-2:
# Напишите скрипт отображающий папки текущей директории
list = os.listdir()
for i in list:
    print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(my_file, backup):
    shutil.copy(my_file, backup)

my_file = sys.argv[0]
backup = my_file + '.backup'
copy_file(my_file,backup)



# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания легко, оформленные в виде соответствующих функций,
#и импортированные в данный файл из easy.py

import os
import sys

#from zadanie_5easy import  os
print('Ваша текущая директория {}'.format(os.getcwd()))

while True:
    print('Перейти в папку - цифра 1\nПросмотреть содержимое текущей папки - цифра 2\nУдалить папку - цифра 3'
          '\nСоздать папку - цифра 4\nДля выхода - введите 0')
    menu = input("Введите цифру: ")

    if menu == '1':
        dir_name = input('Введите путь папки, в которую хотите перейти: ')
        os.chdir(dir_name)
    elif menu == '2':
        os.getcwd()
    elif menu == '3':
        dir_name = input('Введите путь папки, для её удаления: ')
        os.rmdir(dir_name)
    elif menu == '4':
        dir_name = input('Введите путь папки,для её создания: ')
        os.mkdir(dir_name)
    elif menu == '0':
        print('До свидания!')
        break
    else:
        print('Успешно создано/удалено/перешел')



