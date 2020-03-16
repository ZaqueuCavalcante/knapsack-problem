# -*- coding: utf-8 -*-
from random import choices

def realiza_mutacao(nova_populacao, mutantes, taxa_mutacao):
    # Realiza mutação das mochilas selecionadas (mutantes).
    
    quant_mutacoes = (len(nova_populacao[0])*taxa_mutacao)//100
    
    gene_index = []
    for i in range(0, len(nova_populacao[0])):
        gene_index.append(i)
    
    for i in range(0, len(mutantes)):
        cobaia = nova_populacao[mutantes[i][0]]
        for j in range(0, quant_mutacoes):
            index_escolhido = choices(gene_index, k=1)
            
            if (cobaia[index_escolhido[0]] == 0):
                cobaia[index_escolhido[0]] = 1
            else:
                cobaia[index_escolhido[0]] = 0
                
            gene_index.remove(index_escolhido[0])
            
    return nova_populacao
            