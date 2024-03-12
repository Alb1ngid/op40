


#venv, game
# 3 вида модулей

# импорты
from random import randint
# print(randint(1,88))


from random import *
# print(randint(1,88))
# 1 внутренние модули - random

import random,math
# print(random.randint(1,100))

# 2 собвственные модули

# import lesson2
# lesson2.Figure
from lesson2 import Figure
beka=Figure('name',180)
print(beka.vizion())



from learnGeeks import main as car

a=car.Car('bmw',1999,'red')
print(a)

# 3 внешние модули : 1 оболочка для скачивания 2 интерпритатор для вашей idea
import colorama
print(colorama.Back.BLACK,
      colorama.Fore.LIGHTMAGENTA_EX)

print('hello')
from art import tprint

tprint('hello')
