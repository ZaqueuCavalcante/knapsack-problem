# -*- coding: utf-8 -*-
import numpy as np

def funcao_objetivo(valores_mochilas, pesos_mochilas, valor_max, peso_max):
    # Calcula a aptidao da população como solução do problema.
    # Ela leva em conta tanto o valor total da mochila quanto sua posição em 
    # relação à linha de peso máximo. 
    
    aptidoes = []
    
    for i in range(0, len(valores_mochilas)):
        aptidao = valores_mochilas[i]#/valor_max + 2 * 1/(1+np.exp(pesos_mochilas[i]/peso_max))
        aptidoes.append(aptidao)
            
    return aptidoes