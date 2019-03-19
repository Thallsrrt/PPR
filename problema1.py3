#!/usr/bin/python3

valor = int(input())
if valor < 60:
    print()
    print('0 : 0 :', valor)
else:
    print()
    hora = valor // 3600
    valor = valor % 3600
    minuto = valor // 60
    valor = valor % 60
    segundos = valor
    print(hora,':',minuto,':',segundos)
