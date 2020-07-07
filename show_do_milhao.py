# Import
import Game_Show_Milhao
import random

# Variaveis
cont_pergutas = 24
cont_rodada = 0
cont_pulo = 3
moeda = 500
premio_atual = 100
ganhando = True
rodada = '1º'
perguntas = Game_Show_Milhao.Perguntas
respostas = Game_Show_Milhao.Respostas
test_resp = Game_Show_Milhao.Teste_Resp

# Funções


def cls():  # Cria espaços para afastar as perguntas da proxima
    print('\n'*10)


def PulaResponde():  # Verifica se o jogador vai responder ou pular a questão
    global cont_pulo
    print(
        "\033[4;1;31mDigite 'R' para reponder a pergunta ou 'P'para Pular a pergunta?\033[m")
    pula_resp = str(input())
    respondendo = False

    while not respondendo:

        if pula_resp.upper() == 'P':
            cont_pulo -= 1

            if cont_pulo < 0:
                desistir = input(
                    f"Você só tem mais 0 pulos, Se pular nesse momento você estará desistindo.\nDeseja Desistir?'S'para sim 'N' para não.")

                if desistir.upper() == 'N':
                    cont_pulo = 0
                    cls()
                    respondendo = True
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

        else:
            print('Resposta invalida!')
            print(
                "\033[4;1;31mDigite 'R' para reponder a pergunta ou 'P'para Pular a pergunta?\033[m")
            pula_resp = input()


def TestResposta(entrada):  # Verifica se a resposta está contida na test_resp
    global ganhando, premio_atual, moeda, cont_pulo

    if entrada.upper() in test_resp:
        print("Correta resposta!")
        cls()
        moeda += premio_atual
        if moeda >= 1000 and cont_pergutas >= 13:
            premio_atual = 1000
    else:
        cont_pulo = -1
        print(f'Resposta Errada você ganhouR${int(moeda/2)},00.')
        ganhando = False


def Aleatorio():  # Gera uma lista de 0 a 24 e divide para as rodadas
    result = random.sample(range(0, 24), 24)

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


def Pergunta():  # Gera a perguna atravez de uma lista aleatória
    global cont_pergutas
    selecao_rod = Aleatorio()
    for x in range(cont_rodada):

        if ganhando:

            if cont_pulo < 0:
                print(f'Você Desistiu e recebeu R${int(moeda/2)},00!')
                break
            print(selecao_rod)
            # Monta a pergunta apartir do dic_show
            print(
                f'Você tem R${moeda},00.\nNesta rodada você ganhará R${premio_atual},00 caso acerte.')
            print(f'{x+1} - {perguntas[selecao_rod[x]]}')

            # Monta as opções apartir do dic_show
            selecao = random.sample([0, 1, 2, 3], k=4)
            for resposta in range(4):
                print(
                    f'{resposta+1} : {respostas[perguntas.index(perguntas[selecao_rod[x]])][selecao[resposta]]}')

            PulaResponde()

            cont_pergutas -= 1

        else:
            break


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

    print('{:^92}'.format(f'\033[1;34m{rodada} RODADA!\033[m\n'))

    Pergunta()


cls()
print('{:^92}'.format('\033[1;31mBEM VINDO AO SHOW DO MILHÃO!\033[m'))

nome = input('Digite o seu nome:')
print(f"\nOlá, \033[3m{nome.title()}\033[0m. Antes de começar preste atenção nas regras:\nVocê terá que responder a 24 perguntas, separadas por quadro rodadas\ncom 11, 6, 6 e 1 pergunta(s).Na primeira rodada, o participante começa \ncom R$500,00, e a cada acerto, R$100,00 são acrecentados à sua pontuação.\n Quando o você chegar a marca dos R$1000,00, a partir deste ponto o valor \npor acerto sobe para R$1000,00, na segunda rodada, serão feitas 6 perguntas, \ncada uma valendo R$10.000,00. Já na terceira rodada, as perguntas valem R$100.000,00. \nIsso mesmo, são 6 perguntas valendo R$100.000,00. Por fim temos a rodada \nfinal que consiste de uma única pergunta valendo R$1.000.000,00!\nVocê terá 3 chances de pular uma pergunta. \n\033[4;1;31mMAS PRESTE ATENÇÃO, NO PRIMEIRO DESLIZE VOCÊ ESTÁ FORA E RECEBERA A METADE DO CONQUISTADO,\nE ISSO VALE PARA TODAS AS RODADAS COM EXCEÇÃO DA ÚLTIMA RODADA ONDE A DERRROTA CUSTARÁ \nTODO O VALOR ACUMULADO!\033[m \n\n")

s = str(input('Digite qualquer tecla para começar\n'))
cls()

while cont_pulo > 0:

    Rodadas()
