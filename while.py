# -*- coding: utf-8 -*-


def run():
  LIMITE = 1000000
  contador = 0
  pontencia_2 = 1
  while pontencia_2 < LIMITE:
    print('2 elevado a ', contador, ' es igual a ', pontencia_2)
    contador+=1
    pontencia_2=2**contador


if __name__ == '__main__':
  run()