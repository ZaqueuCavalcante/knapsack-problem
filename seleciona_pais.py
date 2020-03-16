# -*- coding: utf-8 -*-
def seleciona_pais(ranking):
    # Retorna uma lista com os pares [mãe, pai].
    # * Remodelar a função depois.
        
    pais_selecionados = []
        
    for i in range(0, len(ranking)-1):
        pais = [ranking[i], ranking[i+1]]
        pais_selecionados.append(pais)

    return pais_selecionados