# -*- coding: utf-8 -*-
from numpy import exp
from numpy import log as ln
from random import choices

def seleciona_pais(ranking):
    # Retorna uma lista com os pares [mãe, pai].
    # Cada mochila do ranking terá uma probabilidade de ser escolhida para ser
    # mãe ou pai. Esta probabilidade é proporcional à posição da mochila no 
    # ranking. 
    
    # Os parâmetros a seguir controlam o comportamento da função de 
    # probabilidade.
    p_max = 0.999    # Prob. da primeira mochila do ranking ser escolhida.
    p_min = 0.001    # Prob. de última mochila ser escolhida. 
        
    pais_selecionados = []
    prob_selecao = []
    n_mochilas = len(ranking)
    
    for i in range(0, n_mochilas):
        prob = p_max / exp(ln(p_max/p_min) * i/(n_mochilas-1))
        prob_selecao.append(prob)
        
    for i in range(0, n_mochilas):        
        pais = choices(ranking, prob_selecao, k=2)        
        pais_selecionados.append(pais)

    return pais_selecionados
