# -*- coding: utf-8 -*-


def run():
  frase = input('Escribe tu frase: ')
  frase=frase.upper()
  for letra in frase:
    print(letra)


if __name__ == '__main__':
  run()