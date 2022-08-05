'''
beecrowd | 1015
Distância Entre Dois Pontos
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = Raiz ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

INPUT = input().split()
X1 = float(INPUT[0])
Y1 = float(INPUT[1])

INPUT = input().split()
X2 = float(INPUT[0])
Y2 = float(INPUT[1])
print(format((((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** (0.5), '.4f'))
