#!/usr/bin/python3

valor = int(input())
print()
ano = valor // 365
valor = valor % 365
print(ano, 'Ano(s)')
meses = valor // 30
valor = valor % 30
print(meses, 'Mes(es)')
print(valor, 'Dia(s)')
