# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def plot_espaco_busca(valores_mochilas, valor_max, pesos_mochilas, peso_limite, peso_max, titulo):
    # Plota a população em um gráfico de espalhamento.
        
    plt.figure(figsize=(16, 10))
    
    for i in range(0, len(pesos_mochilas)):
        if (pesos_mochilas[i] <= peso_limite):
            plt.scatter(pesos_mochilas[i], valores_mochilas[i], color='g')
        else:
            plt.scatter(pesos_mochilas[i], valores_mochilas[i], color='r')
    
    plt.title(titulo, fontweight="bold") 
    plt.xlabel('Pesos (kg)')
    plt.xlim(0, peso_max)
    plt.ylabel('Valores (R$)')
    plt.ylim(0,valor_max)
    plt.grid()
    plt.axvline(x=peso_limite, color='y')
    plt.text(peso_limite, 150, ' Peso \n limite')
    plt.show()

