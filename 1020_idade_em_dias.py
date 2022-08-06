'''
beecrowd | 1020
Idade em Dias
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''

i = int(input())
a = m = 0

while i >= 365:
    i = i - 365
    a += 1

while i >= 30:
    if m < 11:
        i = i - 30
        m += 1
    elif m == 12:
        a += 1
    else:
        i = i - 5

print(f'''{a} ano(s)
{m} mes(es)
{i} dia(s)''')
