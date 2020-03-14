import matplotlib.pyplot as plt

def plot_espaco_busca(valores_mochilas, pesos_mochilas, peso_max, titulo):
    # Plota a população em um gráfico de espalhamento.
    
    plt.rcParams.update({'font.size': 16})
    plt.figure(figsize=(12, 8))
    
    for i in range(0, len(pesos_mochilas)):
        if (pesos_mochilas[i] <= peso_max):
            plt.scatter(pesos_mochilas[i], valores_mochilas[i], color='g')
        else:
            plt.scatter(pesos_mochilas[i], valores_mochilas[i], color='r')
    
    plt.title(titulo, fontweight="bold") 
    plt.xlabel('Pesos (kg)')
    plt.ylabel('Valores (R$)')
    plt.grid()
    plt.axvline(x=peso_max, color='y')
    plt.text(peso_max, 150, ' Peso \n máximo')
