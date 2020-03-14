# - - - > Definição das funções utilizadas no decorrer do programa.

import random

def gera_ranking(aptidao):
    # Gera uma lista dos indivíduos de valores mais altos até os mais baixos.
    # Nela, cada inteiro representa uma mochila.
    # Exemplo: [3,0,1,2]
        # A mochila 3 da população (quarta mochila na lista pop) é a mais aptada.
        # A mochila 0 é a segunda mais apta...

    ranking = []

    for i in range(0, len(aptidao)):
        valor_max = max(aptidao)
        indice = aptidao.index(valor_max)
        ranking.append(indice)
        aptidao[indice] = 0

    return ranking


def cruzamento(pop, nova_pop):
    # Realiza o cruzamento entre os pais para formar a próxima população.

    n_objetos = len(nova_pop[0])

    for i in range(0, len(pop)-1):
        pai = pop[i]
        mae = pop[i+1]
        loc_corte = random.randint(1, n_objetos)
        filho = pai[0:loc_corte] + mae[loc_corte:]
        nova_pop.append(filho)

    return nova_pop

    




