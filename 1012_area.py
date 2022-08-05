'''
beecrowd | 1012
Área
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
'''


def formatted(x):
    return format(x, '.3f')


INPUT = input().split()
A = float(INPUT[0])
B = float(INPUT[1])
C = float(INPUT[2])
# TRIANGULO: Divide por 2 o resultado da multiplicação da base pela altura.
# CIRCULO: O raio elevado ao quadrado vezes pi.
# TRAPEZIO: Soma as bases, multiplica pela altura e divide o resultado por dois.
# QUADRADO: Multiplica a medida do comprimento pela medida da largura.
# RETANGULO: Multiplica a medida do comprimento pela medida da largura.
TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * (C ** 2)
TRAPEZIO = ((A + B) * C)/2
QUADRADO = (B * B)
RETANGULO = (A * B)
print(f'''TRIANGULO: {formatted(TRIANGULO)}
CIRCULO: {formatted(CIRCULO)}
TRAPEZIO: {formatted(TRAPEZIO)}
QUADRADO: {formatted(QUADRADO)}
RETANGULO: {formatted(RETANGULO)}''')
