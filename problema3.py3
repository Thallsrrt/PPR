#!/usr/bin/python3

valor = float(input())

if valor >= 0.0 and valor <= 25.0:
    print('Intervalo 0-25')
elif valor >= 25.01 and valor <= 50.0:
    print('Intervalo 25-50')
elif valor >= 50.01 and valor <= 75.0:
    print('Intervalo 50-75')
elif valor >= 75.01 and valor <= 100.0:
    print('Intervalo 75-100')
elif valor > 100 or valor < 0:
    print('Fora de intervalo')
