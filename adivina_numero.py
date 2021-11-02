# -*- coding: utf-8 -*-

import random

def run():
  aleatorio=random.randint(1,100)
  numero = 0
  while numero != aleatorio:
    numero = int(input('Elige un numero entre 1 y 100: '))
    if numero<aleatorio:
      print('Elige un numero más alto')
    if numero>aleatorio:
      print('Elige un numero más bajo')
  print('Felicidades, ganaste')


if __name__ == '__main__':
  run()