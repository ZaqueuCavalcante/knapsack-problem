# -*- coding: utf-8 -*-
from calcula_valor_mochila import calcula_valor_mochila

def calcula_valor_populacao(populacao, valores):
    # Calcula o valor total de cada mochila da população.

    aptidoes = []

    for mochila in populacao:
        valor_total = calcula_valor_mochila(mochila, valores)
        aptidoes.append(valor_total)

    return aptidoes