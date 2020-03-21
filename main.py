# -*- coding: utf-8 -*-
"""
Source developed in Python 3.7
Zaqueu Cavalcante (zaqueudovale@gmail.com) 
Date: 14/03/2020
"""

from gera_populacao_inicial import gera_populacao_inicial
from calcula_valores_populacao import calcula_valores_populacao
from calcula_pesos_populacao import calcula_pesos_populacao
from plot_espaco_busca import plot_espaco_busca

from funcao_objetivo import funcao_objetivo
from plot_funcao_objetivo import plot_funcao_objetivo
from decodifica_mochila import decodifica_mochila
from gera_ranking import gera_ranking
from seleciona_pais import seleciona_pais
from cruzamento import cruzamento
from seleciona_mutantes import seleciona_mutantes
from realiza_mutacao import realiza_mutacao

from print_lista import print_lista

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

valor_max = sum(valores)    # Valor máximo (mochila com todos os objetos).
peso_max = sum(pesos)    # Peso máximo (mochila com todos os objetos).

# Cada indivíduo será representado através de uma lista, na qual:
    # 0 -> indica que o objeto não está presente na mochila.
    # 1 -> indica que o objeto está presente na mochila.
    # Exemplo de mochila:
        # m = [1,0,0,0,0,0,0,0,1,0] -> apenas o primeiro e o penúltimo objeto 
                                       # estão presentes na mochila.

# 2 - GERAÇÃO DA POPULAÇÃO INICIAL - - - - - - - - - - - - - - - - - - - - - #

tamanho_populacao = 100
peso_limite = 6.5    # Peso limite de uma mochila válida.

populacao = gera_populacao_inicial(tamanho_populacao, n_objetos)

# 3 - CICLO EVOLUTIVO - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

n_geracoes = 20    # Número máximo de gerações (critério de parada).

prob_mutacao = 5    # Probabilidade de ocorrer mutação, em %.
taxa_mutacao = 50    # Quantidade de genes que sofrerão mutação, em %.

for geracao in range(1, n_geracoes+1):
    
    # 4 - AVALIAÇÃO DA APTIDÃO DA POPULAÇÃO ATUAL - - - - - - - - - - - - - - #

    t = 'Espaço de Busca - Geração ' + str(geracao)
    valores_mochilas = calcula_valores_populacao(populacao, valores)
    pesos_mochilas = calcula_pesos_populacao(populacao, pesos)
    plot_espaco_busca(valores_mochilas, valor_max, pesos_mochilas, peso_limite, 
                      peso_max, t)
    
    t = 'Função Objetivo - Geração ' + str(geracao)
    aptidoes = funcao_objetivo(valores_mochilas, pesos_mochilas, valor_max, 
                               peso_limite)
    #plot_funcao_objetivo(valores_mochilas, pesos_mochilas, aptidoes, peso_max, t)
    
    # 5 - RANKING DE APTIDÃO - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # Geração de uma lista das mochilas que compõe a geração atual, por ordem 
    # de aptidão (da maior para a menor).

    ranking = gera_ranking(aptidoes[:])
                
    # 6 - SELEÇÃO DOS PAIS - - - - - - - - - - - - - - - - - - - - - - - - - #

    pais = seleciona_pais(ranking)
    
    # 7 - CRUZAMENTO - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # O método utilizado será o de 'recombinação com um ponto de corte'.

    populacao = cruzamento(populacao, pais)
    
    # 8 - MUTAÇÃO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # Consiste em mudar, aleatoriamente, alguma característica do indivíduo.
    # No caso, algumas mochilas (dentro da nova população) serão selecionadas. 
    # Cada uma delas terá um objeto retirado ou adicionado.
    
    #mutantes = seleciona_mutantes(nova_populacao, prob_mutacao)
    
    #nova_populacao_2 = realiza_mutacao(nova_populacao, mutantes, taxa_mutacao)
    
    # 9 - ATUALIZAR POPULAÇÃO - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # Mostrar população ao final da geração.
    
# 10 - MELHORES SOLUÇÕES - - - - - - - - - - - - - - - - - - - - - - - - - - #
    
# Mostrar a população final.
# Mostrar um top 3 das melhores soluções, usando a decodifica_mochila().
    


        
