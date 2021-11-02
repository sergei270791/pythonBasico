# -*- coding: utf-8 -*-

def palindromo(palabra):
  palabra = palabra.replace(' ','')
  palabra = palabra.lower()
  palabra_invertida = palabra[::-1]
  if palabra == palabra_invertida:
    return True
  return False


def run():
  palabra = input('Escribe la palabra: ')
  es_palindromo = palindromo(palabra)
  if es_palindromo:
    print("Es palindroma")
  else: 
    print("No es palindroma")


if __name__ == '__main__':
  run()

