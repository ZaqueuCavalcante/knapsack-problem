# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_funcao_objetivo(valores_mochilas, pesos_mochilas, aptidoes, peso_max, titulo):
    # Plota a aptidão da mochila em função do seu valor e peso.
    
    figura = plt.figure(figsize=(16, 10))
    quadro = figura.add_subplot(1, 1, 1)
    quadro = figura.gca(projection='3d')
    
    # PLOTAR COM BARRA DE CORES. MAIS ALTO VALOR, MAIS QUENTE/VERMELHO. TIPO ANSYS.
    
    for i in range(0, len(pesos_mochilas)):
        if (pesos_mochilas[i] <= peso_max):
            quadro.scatter(pesos_mochilas[i], valores_mochilas[i], aptidoes[i], color='b')
        else:
            quadro.scatter(pesos_mochilas[i], valores_mochilas[i], aptidoes[i], color='b')
    
    plt.title(titulo, fontweight="bold") 
    quadro.set_xlabel('Pesos (kg)')
    quadro.set_ylabel('Valores (R$)')
    quadro.set_zlabel('Aptidão ')
    plt.grid()
    # Traçar plano.
    #plt.axvline(x=peso_max, color='y')
    #plt.text(peso_max, 150, ' Peso \n máximo')    
    plt.show()  
    
    