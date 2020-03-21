# -*- coding: utf-8 -*-

def funcao_objetivo(valores_mochilas, pesos_mochilas, valor_max, peso_max):
    # Calcula a aptidao da população como solução do problema.
    # Ela leva em conta tanto o valor total da mochila quanto sua posição em 
    # relação à linha de peso máximo. 
    
    aptidoes = []
    
    for i in range(0, len(valores_mochilas)):
        if (pesos_mochilas[i] <= peso_max):
            auxiliar = pesos_mochilas[i]/peso_max
        else:
            auxiliar = - 0.8
        aptidao = valores_mochilas[i]/valor_max + auxiliar
        aptidoes.append(aptidao)
            
    return aptidoes