# -*- coding: utf-8 -*-
from calcula_peso_mochila import calcula_peso_mochila
from calcula_valor_mochila import calcula_valor_mochila

def decodifica_mochila(mochila, nomes, valores, pesos):
    # Retorna todos os objetos presentes na mochila, bem como seu peso e valor.
    
    mochila_decodificada = []
            
    for i in range(0, len(mochila)):
        if (mochila[i] == 1):
            mochila_decodificada.append(nomes[i])

    valor_mochila = calcula_valor_mochila(mochila, valores)
    peso_mochila = calcula_peso_mochila(mochila, pesos)
    
    mochila_decodificada.append('-------------------')    
    mochila_decodificada.append('Valor: R$ ' + str(valor_mochila))
    mochila_decodificada.append('Peso: ' + str(peso_mochila) + ' kg')
    
    return mochila_decodificada