# -*- coding: utf-8 -*-
def calcula_valor_mochila(mochila, valores):
    # Calcula a soma dos valores de todos os objetos presentes na mochila.

    valor_mochila = 0
    
    for i in range(0, len(mochila)):
        valor_objeto = valores[i]     
        zero_ou_um = mochila[i]     
        valor_mochila += zero_ou_um*valor_objeto

    return valor_mochila