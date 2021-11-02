# -*- coding: utf-8 -*-
def es_primo(n):
  if n==2:
    return True
  for i in range(2,n):
    if n%i == 0:
      return False
    continue
    return True




def run():
  numero = int(input('Escribe un numero: '))
  if es_primo(numero):
    print("Es primo")
  else: 
    print("No es primo")


if __name__ == '__main__':
  run()