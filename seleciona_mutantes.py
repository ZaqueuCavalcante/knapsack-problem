# -*- coding: utf-8 -*-
from random import choices

def seleciona_mutantes(nova_populacao, prob_mutacao):
    # Seleciona quais mochilas, aleatoriamente, sofrerão mutação.
        
    pop_index = []
    for i in range(0, len(nova_populacao)):
        pop_index.append(i)
    
    mutantes = []
    quant_mutantes = (len(nova_populacao)*prob_mutacao)//100
    
    for i in range(0, quant_mutantes):
        index_escolhido = choices(pop_index, k=1)
        mutantes.append(index_escolhido)
        pop_index.remove(mutantes[i][0])
        
    return mutantes