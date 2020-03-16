# -*- coding: utf-8 -*-
from calcula_peso_mochila import calcula_peso_mochila

def calcula_peso_populacao(populacao, pesos):
    # Calcula o peso total de cada mochila da população.

    pesos_mochilas = []

    for mochila in populacao:
        peso_total = calcula_peso_mochila(mochila, pesos)
        pesos_mochilas.append(peso_total)

    return pesos_mochilas