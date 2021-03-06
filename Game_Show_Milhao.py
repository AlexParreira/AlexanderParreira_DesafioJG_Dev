"""
Programa: DeafioJG_Dev
Autor: Alexander de Oliveira Parreira
Turma: Super Esteg Jovem Gênios
Data da Entrega:07/07/2020
Descrição:
    O software consiste em um game em linha de comando que reproduz parte do jogo O Show do Milhão.
"""
from show_do_milhao import *

# Listas de Perguntas
Perguntas = [
    'Em que estado brasileiro nasceu a apresentadora Xuxa?\n',
    'Qual é o nome dado ao estado da água em forma de gelo?\n',
    'Qual era o apelido da cantora Elis Regina?\n',
    'Quem é a namorada do Mickey?\n',
    'Qual é o personagem do folclore brasileiro que tem uma perna só?\n',
    'Fidel Castro nasceu em que país?\n',
    'Quem proclamou a república no Brasil em 1889?\n',
    'Quem é o patrono do exército brasileiro?\n',
    'Quem era o apresentador que reprovava os calouros tocando uma buzina?\n',
    'O que era Frankenstein, de Mary Shelley?\n',
    'Qual é o signo do zodíaco de quem nasce no dia do ano-novo?\n',
    'Quem fundou a fábrica de automóveis Ford?\n',
    'Qual é a cor que se associa com os grupos ecológicos?\n',
    'A água ferve a quantos graus centígrados?\n',
    'Quando é comemorado o dia da independência do Brasil?\n',
    'Qual lugar é também chamado de Santa Sé?\n',
    'Quem tem por lema a frase: “Sempre alerta”?\n',
    'Quem foi o grande amor de Julieta?\n',
    'Quantos signos formam o zodíaco?\n',
    'Vatapá é uma comida típica de qual estado?\n',
    'Como se chama o lugar onde são armazenadas as balas de um revólver?\n',
    'Qual personagem da turma da Mônica tem apenas cinco fios de cabelo?\n',
    'Qual cantora tinha o apelido de “Ternurinha” na época da jovem guarda?\n',
    'O churrasco é considerado uma comida típica de qual estado?\n',

]
# Dict com as opçoes da respostas
Respostas = {
    0: ['RIO DE JANEIRO', 'RIO GRANDE DO SUL', 'SANTA CATARINA', 'GOIÁS'],
    1: ['LÍQUIDO', 'SÓLIDO', 'GASOSO', 'VAPOROSO'],
    2: ['GAUCHINHA',  'PIMENTINHA', 'PAULISTINHA', 'ANDORINHA'],
    3: ['MARGARIDA', 'MINNIE', 'A PEQUENA SEREIA', 'OLÍVIA PALITO'],
    4: ['CUCA', 'SACI-PERERÊ', 'NEGRINHO DO PASTOREIO', 'BOITATÁ'],
    5: ['JAMAICA', 'CUBA', 'EL SALVADOR', 'MÉXICO'],
    6: ['ZÈ DA ESQUINA', 'MARECHAL DEODORO', 'MARECHAL RONDON', 'DOM PEDRO II'],
    7: ['ZÈ DA ESQUINA', 'DUQUE DE CAXIAS', 'BARÃO DE MAUÁ',  'MARQUÊS DE POMBAL'],
    8: ['RAUL GIL', 'CHACRINHA', 'BOLINHA', 'FLÁVIO CAVALCANTI'],
    9: ['GORILA', 'MONSTRO', 'PRÍNCIPE', 'SAPO'],
    10: ['VIRGEM', 'CAPRICÓRNIO', 'AQUÁRIO',  'ÁRIES'],
    11: ['HARRISON FORD', 'HENRY FORD', 'GERALD FORD',  'ANNA FORD'],
    12: ['PRETA', 'VERDE', 'VERMELHA', 'AZUL'],
    13: ['200', '100', '170', '220'],
    14: ['21 DE ABRIL', '7 DE SETEMBRO', '12 DE OUTUBRO', '25 DE DEZEMBRO'],
    15: ['VENEZA', 'VATICANO', 'VITÓRIA', 'VANCOUVER'],
    16: ['MÉDICOS', 'ESCOTEIROS', 'BOMBEIROS', 'POLICIAIS'],
    17: ['ORFEU', 'ROMEU', 'HAMLET', 'IAGO'],
    18: ['NOVE', 'DOZE', 'DEZ', 'ONZE', ],
    19: ['SANTA CATARINA', 'PARANÁ', 'SÃO PAULO', 'BAHIA'],
    20: ['TAMBOR', 'CANO',  'AGULHA', 'GATILHO'],
    21: ['MÔNICA', 'CEBOLINHA', 'CASCÃO', 'MAGALI'],
    22: ['SILVINHA', 'WANDERLÉIA', 'GRETCHEN', 'MARTINHA'],
    23: ['CEARÁ', 'RIO GRANDE DO SUL', 'PARÁ', 'MARANHÃO'],
}

# Lista com respostas corretas
Teste_Resp = [
    'RIO GRANDE DO SUL',
    'SACI-PERERÊ',
    'SÓLIDO',
    'PIMENTINHA',
    'ESCOTEIROS',
    'VERDE',
    'MINNIE',
    'CUBA',
    'MARECHAL DEODORO',
    'DUQUE DE CAXIAS',
    'CHACRINHA',
    'MONSTRO',
    'CAPRICÓRNIO',
    'HENRY FORD',
    '100',
    '7 DE SETEMBRO',
    'VATICANO',
    'ROMEU',
    'DOZE',
    'PARANÁ',
    'TAMBOR',
    'CEBOLINHA',
    'WANDERLÉIA',
]
