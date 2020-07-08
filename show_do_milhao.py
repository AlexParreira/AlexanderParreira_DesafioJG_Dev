"""
Programa: DeafioJG_Dev
Autor: Alexander de Oliveira Parreira
Turma: Super Esteg Jovem Gênios
Data da Entrega:07/07/2020
Descrição:
    O software consiste em um game em linha de comando que reproduz parte do jogo O Show do Milhão.
"""

# Import
import Game_Show_Milhao
import random

# Variaveis
perguntas = Game_Show_Milhao.Perguntas
respostas = Game_Show_Milhao.Respostas
test_resp = Game_Show_Milhao.Teste_Resp
cont_pergutas = 24      # conta  perguntas passaram
cont_rodada = 0         # conta quantas perguntas terá a rodada
cont_pulo = 3           # armazena contagen de pulos restantes
cont_ajuda = 2          # armazena contagen de ajudas restantes
x_pergunta = 0          # armazena o valor atual do for dentro do Pergunta()
ctl_pergunta = 0        # armazena o valor do Aleatorio() dentro do Pergunta()
# controla o temanho que terá o range do Aleatorio()
ctl_result = len(perguntas)
moeda = 500             # controla a quantidade de dinheiro
premio_atual = 100      # controla o premio da rodada
jogando = True          # verifica se o jogador esta ou não repondendo
rodada = '1º'           # controla a rodada aula
# controla a geração de resposta sempre aleatoria independente do index original
selecao = ''


# Funções

def cls():  # Cria espaços para afastar as perguntas da proxima
    print('\n'*5)


def Pergunta():  # Gera a perguna atravez de uma lista aleatória
    global cont_pergutas, x_pergunta, ctl_pergunta, selecao

    selecao_rod = Aleatorio()
    ctl_pergunta = selecao_rod

    for x in range(cont_rodada):

        x_pergunta = x
        # gera um ordem aleatória para as respostas
        selecao = random.sample([0, 1, 2, 3], k=4)

        if jogando:

            if cont_pulo < 0:
                print(f'Você Desistiu e recebeu R${int(moeda/2)},00!')
                break

            # Monta a pergunta apartir do Game_Show_Milhao
            print(
                f'Você tem R${moeda},00.\nValendo R${premio_atual},00!\n')
            print(f'{x+1} - {perguntas[selecao_rod[x]]}')

            # Monta as opções apartir do Game_Show_Milhao
            for resposta in range(4):
                print(
                    f'{resposta+1} : {respostas[perguntas.index(perguntas[selecao_rod[x]])][selecao[resposta]]}')

            PulaRespondeAjuda()

            cont_pergutas -= 1

        else:
            break


def Ajuda():  # Monta a pergunta pintando de vermelho 2 respostas aleatória
    cls()
    print(f'{x_pergunta+1} - {perguntas[ctl_pergunta[x_pergunta]]}')

    cor_ajuda = 0
    for resposta in range(4):

        if not respostas[perguntas.index(perguntas[ctl_pergunta[x_pergunta]])][selecao[resposta]] in test_resp:
            if cor_ajuda < 2:
                print(
                    f'\033[1;4;31m{resposta+1} : {respostas[perguntas.index(perguntas[ctl_pergunta[x_pergunta]])][selecao[resposta]]}\033[m')
                cor_ajuda += 1
            else:
                print(
                    f'{resposta+1} : {respostas[perguntas.index(perguntas[ctl_pergunta[x_pergunta]])][selecao[resposta]]}')
        else:
            print(
                f'{resposta+1} : {respostas[perguntas.index(perguntas[ctl_pergunta[x_pergunta]])][selecao[resposta]]}')
    cor_ajuda = 0
    ent_resp = input("Digite sua resposta: ")
    TestResposta(ent_resp)


def PulaRespondeAjuda():  # Verifica se o jogador vai responder ou pular ou pedir ajuda
    global cont_pulo, cont_ajuda
    print(
        "\033[4;1;32mDigite 'R' para reponder a pergunta\nDigite 'P'para Pular a pergunta\nDigite 'J' para receber ajuda?\033[m")
    pula_resp = str(input())
    respondendo = False

    while not respondendo:

        if pula_resp.upper() == 'P':
            cont_pulo -= 1

            if cont_pulo < 0:
                desistir = input(
                    f"Você só tem mais 0 pulos, Se pular nesse momento você estará desistindo.\nDeseja Desistir?'S'para sim 'N' para não.")

                if desistir.upper() == 'N':
                    cls()
                    cont_pulo = 0
                    print(
                        f'{x_pergunta+1} - {perguntas[ctl_pergunta[x_pergunta]]}')

                    for resposta in range(4):
                        print(
                            f'{resposta+1} : {respostas[perguntas.index(perguntas[ctl_pergunta[x_pergunta]])][selecao[resposta]]}')
                    PulaRespondeAjuda()

                else:
                    respondendo = True
            else:
                cls()
                print(f'Você usou um pulo restam apenas {cont_pulo} pulo/s')
                respondendo = True

        elif pula_resp.upper() == 'R':
            ent_resp = input("Digite sua resposta: ")
            TestResposta(ent_resp)
            respondendo = True

        elif pula_resp.upper() == 'J':
            cont_ajuda -= 1
            if cont_ajuda >= 0:
                print(
                    f'Você usou uma ajuda. Agora só resta {cont_ajuda} ajuda')
                Ajuda()
                respondendo = True
            else:
                print(
                    "\033[4;1;32mVocê não possui mais ajudas!\nDigite 'R' para reponder a pergunta\nDigite 'P'para Pular a pergunta\n\033[m")
                pula_resp = input()

        else:
            print('Resposta invalida!')
            print(
                "\033[4;1;32mDigite 'R' para reponder a pergunta\nDigite 'P'para Pular a pergunta\nDigite 'J' para receber ajuda?\033[m")
            pula_resp = input()


def TestResposta(entrada):  # Verifica se a resposta está contida na test_resp
    global jogando, premio_atual, moeda, cont_pulo

    if entrada.upper() in test_resp:
        print("Correta resposta!")
        cls()
        moeda += premio_atual
        if moeda >= 1000 and cont_pergutas >= 13:
            premio_atual = 1000
    else:
        cont_pulo = -1
        print(f'Resposta Errada! Você ganhou R${int(moeda/2)},00.')
        jogando = False


def Aleatorio():  # Gera uma lista de 0 a 24 e divide para as rodadas
    result = random.sample(range(0, ctl_result), 24)

    if rodada == '1º':
        return result[0:11]
    elif rodada == '2º':
        return result[11:17]
    elif rodada == '3º':
        return result[17:23]
    else:
        final = result[23]
        final = [final]
        return final


def Rodadas():  # Verifica o valor do premio e a contagem de rodada  de acordo com o cont_pergutas
    global rodada, premio_atual, moeda, cont_pergutas, cont_rodada

    if cont_pergutas > 13:
        rodada = '1º'
        premio_atual = 100
        cont_rodada = 11

    elif cont_pergutas > 7 and cont_pergutas <= 13:
        rodada = '2º'
        cont_rodada = 6
        premio_atual = 10000

    elif cont_pergutas > 1 and cont_pergutas <= 7:
        rodada = '3º'
        cont_rodada = 6
        premio_atual = 100000

    else:
        rodada = 'Final'
        cont_rodada = 1
        premio_atual = 1000000

    print('{:^92}'.format(f'\033[1;34m{rodada} RODADA!\033[m'))
    print('{:^82}'.format(f'Nesta rodada o premio é de R${premio_atual},00! \n'))

    Pergunta()
    if moeda >= 1000000:
        print('Parabens! Você acaba de conquistar o premio de 1 MILHÂO de reais.')


cls()
print(f'\033[1;36mby AlexPArreira.\033[m\n')
cls()
print('{:^92}'.format('\033[1;47;30mBEM VINDO AO SHOW DO MILHÃO!\033[m'))
cls()

nome = input('Digite o seu nome:')
print(f"\nOlá, \033[3m{nome.title()}\033[0m. Antes de começar preste atenção nas regras:\nVocê terá que responder a 24 perguntas, separadas por quatro rodadas\ncom 11, 6, 6 e 1 pergunta(s). Na primeira rodada, o participante começa \ncom R$500,00, e a cada acerto, R$100,00 são acrecentados à sua pontuação.\nQuando o jogador chegar a marca dos R$1000,00, a partir deste ponto o valor de\n R$100,00 sobe para R$1000,00, na segunda rodada, serão feitas 6 perguntas, \ncada uma valendo R$10.000,00. Já na terceira rodada, as perguntas valem R$100.000,00. \nIsso mesmo, são 6 perguntas valendo R$100.000,00. Por fim temos a rodada \nfinal que consiste de uma única pergunta valendo R$1.000.000,00!\nVocê terá 3 chances de pular uma pergunta e 2 chances de ajuda,\nmas ao utilizar ajuda deverá respoder a pergunta.\n \n\033[4;1;31mMAS PRESTE ATENÇÃO, NO PRIMEIRO DESLIZE VOCÊ ESTÁ FORA E RECEBERÁ A METADE DO CONQUISTADO,\nE ISSO VALE PARA TODAS AS RODADAS COM EXCEÇÃO DA ÚLTIMA RODADA ONDE A DERRROTA CUSTARÁ \nTODO O VALOR ACUMULADO!\033[m \n\n")

s = str(input('Digite qualquer tecla para começar\n'))
cls()

while cont_pulo > 0:

    Rodadas()
if moeda >= 1000000:
    print('Parabens! Você acaba de conquistar o premio de 1 MILHÂO de reais.')
