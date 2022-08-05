'''
beecrowd | 1018
Cédulas
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1_000_000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''


def formatted(x):
    return format(x, '.2f')


N1 = int(input())
NS = N1
list1 = [100, 50, 20, 10, 5, 2, 1]
list2 = []
for n in list1:
    count = 0
    while n <= N1:
        N1 = N1 - n
        count += 1

    list2.append(count)

print(NS)
for y in range(len(list1)):
    print(f'{list2[y]} nota(s) de R$ {list1[y]},00')
