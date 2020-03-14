# -*- coding: utf-8 -*-
"""
Source developed in Python 3.7
Zaqueu Cavalcante (zaqueudovale@gmail.com) 
Date: 14/03/2020
"""

from gera_populacao_inicial import gera_populacao_inicial
from print_lista import print_lista
from calcula_valor_populacao import calcula_valor_populacao
from calcula_peso_populacao import calcula_peso_populacao
from plot_espaco_busca import plot_espaco_busca
from funcao_objetivo import funcao_objetivo
from plot_funcao_objetivo import plot_funcao_objetivo

# 1 - REPRESENTAÇÃO DE CADA INDIVÍDUO - - - - - - - - - - - - - - - - - - - - # 

# Lista de objetos que podem ser adicionados à mochila, cada qual com 
# determinado valor e peso.
# Cada lista [nome, valor, peso] representa um objeto.
# O valor está em R$ e o peso em kg.

objetos = [['Caneta', 1.5, 0.1], 
           ['Mouse', 50, 0.2], 
           ['Caderno', 60, 1.0], 
           ['Carregador', 100, 0.5], 
           ['Post-it', 5, 0.1], 
           ['Livro', 120, 0.6], 
           ['Notebook', 110, 3.0], 
           ['Smartphone', 90, 0.4], 
           ['Garrafa', 30, 1.5], 
           ['Pen-drive', 80, 0.05], 
           ['Calculadora', 120, 0.5],
           ['Pasta', 25, 0.8]]

n_objetos = len(objetos)
nomes, valores, pesos  = [], [], []

for i in range(0, n_objetos):
    nomes.append(objetos[i][0])   
    valores.append(objetos[i][1]) 
    pesos.append(objetos[i][2])   

# Cada indivíduo será representado através de uma lista, na qual:
    # 0 -> indica que o objeto não está presente na mochila.
    # 1 -> indica que o objeto está presente na mochila.
    # Exemplo de mochila:
        # m = [1,0,0,0,0,0,0,0,1,0] -> apenas o primeiro e o penúltimo objeto 
                                       # estão presentes na mochila.

# 2 - GERAÇÃO DA POPULAÇÃO INICIAL - - - - - - - - - - - - - - - - - - - - - #

tamanho_populacao = 100
peso_max = 6.5    # Peso máximo de uma mochila válida.

populacao_inicial = gera_populacao_inicial(tamanho_populacao, n_objetos)

# 3 - AVALIAÇÃO DA APTIDÃO DA POPULAÇÃO INICIAL - - - - - - - - - - - - - - - #

t = 'Espaço de Busca - População Inicial'
valores_mochilas = calcula_valor_populacao(populacao_inicial, valores)
pesos_mochilas = calcula_peso_populacao(populacao_inicial, pesos)
plot_espaco_busca(valores_mochilas, pesos_mochilas, peso_max, t)

t = 'Função Objetivo - População Inicial'
aptidoes = funcao_objetivo(valores_mochilas, pesos_mochilas, peso_max)
plot_funcao_objetivo(valores_mochilas, pesos_mochilas, aptidoes, peso_max, t)

# 4 - CICLO EVOLUTIVO - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

n_geracoes = 100    # Número máximo de gerações (critério de parada).








        
