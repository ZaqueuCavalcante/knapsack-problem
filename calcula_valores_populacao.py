# -*- coding: utf-8 -*-
from calcula_valor_mochila import calcula_valor_mochila

def calcula_valores_populacao(populacao, valores):
    # Calcula o valor total de cada mochila da população.

    valores_mochilas = []

    for mochila in populacao:
        valor_total = calcula_valor_mochila(mochila, valores)
        valores_mochilas.append(valor_total)

    return valores_mochilas