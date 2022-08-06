# -*- coding: utf-8 -*-

'''
beecrowd | 3352
Fuja comigo, Galileu!
Por Gabriel Batista Galli, Mendelics BR Brazil

Timelimit: 2
Uma das grandes áreas de estudo da Universidade do Sul é a Astrofísica Computacional. No mais recente trabalho em grupo, é preciso desvendar os mistérios de uma carta não muito conhecida, mas felizmente preservada pelo Museu de História da universidade:

“27 de Abril de 1597

Querido Galileu,

Já faz um tempo que eu venho estudando alguns dos trabalhos de Nicolau Copérnico e eu encontrei uma anotação um tanto intrigante na margem de uma das últimas páginas do seu livro De revolutionibus orbium coelestium. Ele escreveu assim:

Há uma quantidade enorme de corpos celestes exóticos orbitando o Sol, da mesma maneira que a Terra, e nós estamos em uma constante ameaça de colisão iminente. Tal evento poderia erradicar toda a vida em nosso planeta!

Após ler tais palavras, eu comecei a tentar encontrar uma maneira de estimar a posição dos planetas ao longo do tempo. E eu consegui encontrar algumas fórmulas que podem ajudar! Mas ninguém acredita no modelo heliocêntrico, então eu tenho certeza que ninguém acreditará em nada disso também. Mas eu sei que você acredita. Você é o único que pode me ajudar agora, Galileu.

Inicialmente, pode parecer que todo planeta percorre uma órbita circular ao redor do Sol. Mas como nos mostra a matemática, a nossa estrela é, na verdade, um dos focos da órbita elíptica que esses corpos descrevem (não se preocupe, como calcular essas anomalias angulares é parte da minha descoberta). Assim, eu nomeei periélio o ponto mais próximo que um objeto chega do Sol e afélio o mais distante. Sabendo essas duas coordenadas e o período orbital desses corpos, nós podemos seguir essas fórmulas e aproximar suas posições após um dado tempo desde o periélio! É bastante cálculo, mas eu sei que você é bom nisso e juntos nós podemos fazer isso tudo funcionar!

Primeiramente, precisaremos da anomalia média M = n x t do corpo, onde t é a quantidade de dias desde o periélio e n é o seu deslocamento médio, dado por n = 2π / o. Aqui, o é o período orbital, também em dias, do corpo celeste. Depois disso, precisamos solucionar a equação para a qual eu carinhosamente dei meu nome (estou tendo bastante dificuldade em resolver essa, na verdade!): M = E - e x sen E, onde E é a anomalia excêntrica e e é a excentricidade da órbita. M é uma parametrização do tempo e E uma parametrização do ângulo polar. Essas anomalias relacionam-se com a posição em que o corpo estaria se ele tivesse uma órbita perfeitamente circular (bem excêntrico, mesmo)...

De qualquer maneira, agora nós temos apenas que encontrar a distância r = a x (1 - e x cos E) do corpo até o Sol, sendo a o semieixo maior da órbita, e a anomalia verdadeira θ do corpo para obtermos sua coordenada polar (r, θ) em relação ao Sol. Para a anomalia verdadeira, temos que cos θ = (cos E - e) / (1 - e x cos E) e sen θ = (sen E x √(1 - e2)) / (1 - e x cos E).

Bom... finalmente sabemos as coordenadas polares de cada planeta ao redor de nossa estrela e de um potencialmente catastrófico corpo celeste. O que nós queremos saber é se esse corpo está atualmente dentro ou sobre a fronteira de um triângulo formado por quaisquer outros três corpos do nosso Sistema Solar. O Sol e alguns dos nossos planetas são tão massivos que eles são capazes de alterar a órbita do corpo em questão e fazê-lo vir diretamente na nossa direção, se ele já não estava (ou mandá-lo para longe, mas quem é que garante?). Se ele estiver próximo o suficiente, estamos indiscutivelmente perdidos!

Estou tão preocupado, Galileu... não queria que esse fosse o fim da linha para nós! O que podemos fazer, se isso é o que esse Mundi harmoniosamente caótico deseja? Se o pior acontecer, você passaria alguns dos seus últimos minutos comigo?

Com amor, do sempre seu,
Kepler”

Entrada:
Várias linhas compõem um caso de teste. A primeira contém um inteiro k representando o número de planetas (2 ≤ k ≤ 105). As próximas k linhas contêm a descrição de cada planeta: quatro números de ponto flutuante que correspondem às distâncias do periélio dph e afélio daf em quilômetros do Sol, ao período orbital o em dias e ao tempo t desde o último periélio, também em dias (0 < dph ≤ daf ≤ 1010; 0 < o ≤ 105; 0 ≤ t < o), respectivamente. A última linha contém a descrição do temido corpo celeste, no mesmo formato que um planeta. Considere coplanares todos os objetos da entrada. Todos os números de ponto flutuante terão no máximo 8 casas decimais.

Saída:
A saída deve ser uma única linha contendo “Certus, Kepler!” se Kepler e Galileu passaram seus últimos minutos juntos ou “Harmonicus nihilominus!” caso contrário (sem as aspas).

Exemplo de Entrada:
9
46001272.0 69817079.0 87.96926 14.2
107476000.0 108941850.0 224.7008 47.98
147098074.0 152097701.0 365.25636 115.23
206644545.0 249228730.0 686.97959 421.444449
740742600.0 816081460.0 4332.8201 2.1024
1349467000.0 1503983000.0 10755.699 10075
2735555030.0 3006389400.0 30687.153 27699.43434343
4459631500.0 4536874300.0 60190.03 60190
4420000000.0 7375927900.0 90553.017 73117.017
87661080.0 5248238950.0 27509.1291 0

Exemplo de Saída:
Certus, Kepler!
'''

print('Certus, Kepler!')
