def funcao_objetivo(valores_mochilas, pesos_mochilas, peso_max):
    # Calcula a aptidao da população como solução do problema.
    # Ela leva em conta tanto o valor total da mochila quanto sua posição em 
    # relação à linha de peso máximo. 
    
    aptidoes = []
    
    for i in range(0, len(valores_mochilas)):
        if (pesos_mochilas[i] > 0):    # Prevenção de divisão por zero.
            aptidao = valores_mochilas[i] + valores_mochilas[i]/(pesos_mochilas[i]/peso_max)
            aptidoes.append(aptidao)
        else:
            aptidao = 0
            aptidoes.append(aptidao)
    
    return aptidoes