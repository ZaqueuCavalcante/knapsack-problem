# -*- coding: utf-8 -*-
def gera_ranking(aptidoes):
    # Gera uma lista das mochilas, em função da sua aptidão.
    # Nessa lista, cada inteiro representa uma mochila.
    # Exemplo: [3,0,8,2,15...]
        # A mochila 3 da população é a mais apta.
        # A mochila 0 é a segunda mais apta...

    ranking = []

    for i in range(0, len(aptidoes)):
        valor_max = max(aptidoes)
        indice = aptidoes.index(valor_max)
        ranking.append(indice)
        aptidoes[indice] = -1

    return ranking