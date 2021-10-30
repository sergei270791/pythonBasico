# -*- coding: utf-8 -*-

menu='''
Hola 🤗, bienvenido a tu conversor de monedas 💵

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos mexicanos
4. Soles

Elige una opcion: '''

opcion=int(input(menu))

if opcion==1:
  valor_dolar=3766.87
elif opcion==2:
  valor_dolar=99.70
elif opcion==3:
  valor_dolar=20.56
else:
  valor_dolar=3.95

cantidad= float(input('Inserte la cantidad a convertir: '))
dolares= cantidad/valor_dolar
dolares=round(dolares,2)  # sirve para redondear a las cifras necesarias
print('Tienes ',dolares,' dolares') 