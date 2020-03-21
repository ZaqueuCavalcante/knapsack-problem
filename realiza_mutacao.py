# -*- coding: utf-8 -*-
from random import choices

def realiza_mutacao(populacao, mutantes, taxa_mutacao):
    # Realiza mutação das mochilas selecionadas (mutantes).
    
    quant_mutacoes = (len(populacao[0])*taxa_mutacao)//100
    
    for i in range(0, len(mutantes)):
        
        gene_index = []
        for j in range(0, len(populacao[0])):
            gene_index.append(j)
        
        cobaia = populacao[mutantes[i][0]]
        
        for k in range(0, quant_mutacoes):
            index_escolhido = choices(gene_index, k=1)
            
            if (cobaia[index_escolhido[0]] == 0):
                cobaia[index_escolhido[0]] = 1
            else:
                cobaia[index_escolhido[0]] = 0
                
            gene_index.remove(index_escolhido[0])
            
    return populacao            