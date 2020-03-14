def calcula_peso_mochila(mochila, pesos):
    # Calcula o peso da mochila passada como parâmetro.

    peso_mochila = 0
        
    for i in range(0, len(mochila)):
        peso_objeto = pesos[i]     
        zero_ou_um = mochila[i]     
        peso_mochila += zero_ou_um*peso_objeto

    return peso_mochila