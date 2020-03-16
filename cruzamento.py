# -*- coding: utf-8 -*-
from random import randint

def cruzamento(populacao, pais):
    # Realiza o cruzamento entre os pais para formar a próxima população.

    n_objetos = len(populacao[0])
    nova_populacao = []
    nova_populacao.append(populacao[0])    # Elitismo sobre a melhor mochila.

    for i in range(0, len(pais)):
        mae_index = pais[i][0]
        pai_index = pais[i][1]
        mae = populacao[mae_index]
        pai = populacao[pai_index]
        local_corte = randint(1, n_objetos)
        # O lado esquerdo vem da mãe e o direito do pai.
        filho = mae[0:local_corte] + pai[local_corte:]
        nova_populacao.append(filho)

    return nova_populacao