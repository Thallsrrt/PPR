#!/usr/bin/python3

valor = float(input())
print(valor)

if valor > 0 and valor <= 400:
    juros = (valor * 0.15)
    valor = valor + juros
    print('Novo salário:', valor)
    print('Reajuste ganho:', juros)
    print('Em percentual: 15%')
elif valor >= 400.01 and valor <= 800:
    juros = (valor * 0.12)
    valor = valor + juros
    print('Novo salário:', valor)
    print('Reajuste ganho:', juros)
    print('Em percentual: 12%')
elif valor >= 800.01 and valor <= 1200:
    juros = (valor * 0.10)
    valor = valor + juros
    print('Novo salário:', valor)
    print('Reajuste ganho:', juros)
    print('Em percentual: 10%')
elif valor >= 1200.01 and valor <= 2000:
    juros = (valor * 0.07)
    valor = valor + juros
    print('Novo salário:', valor)
    print('Reajuste ganho:', juros)
    print('Em percentual: 7%')
elif valor > 2000:
    juros = (valor * 0.04)
    valor = valor + juros
    print('Novo salário:', valor)
    print('Reajuste ganho:', juros)
    print('Em percentual: 4%')
