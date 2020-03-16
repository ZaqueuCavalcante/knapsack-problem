# -*- coding: utf-8 -*-
from gera_mochila_aleatoria import gera_mochila_aleatoria

def gera_populacao_inicial(tamanho_populacao, n_objetos):
    # Gera uma população inicial de mochilas.
    
    populacao_inicial = []
    
    for i in range(0, tamanho_populacao):
        mochila_aleatoria = gera_mochila_aleatoria(n_objetos)
        populacao_inicial.append(mochila_aleatoria)

    return populacao_inicial