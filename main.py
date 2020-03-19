# -*- coding: utf-8 -*-
"""
Source developed in Python 3.7
Zaqueu Cavalcante (zaqueudovale@gmail.com) 
Date: 14/03/2020
"""

from gera_populacao_inicial import gera_populacao_inicial
from calcula_valor_populacao import calcula_valor_populacao
from calcula_peso_populacao import calcula_peso_populacao
from plot_espaco_busca import plot_espaco_busca
from funcao_objetivo import funcao_objetivo
from plot_funcao_objetivo import plot_funcao_objetivo
from decodifica_mochila import decodifica_mochila
from gera_ranking import gera_ranking
from seleciona_pais import seleciona_pais
from cruzamento import cruzamento
from seleciona_mutantes import seleciona_mutantes
from realiza_mutacao import realiza_mutacao

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

tamanho_populacao = 25
peso_max = 6.5    # Peso máximo de uma mochila válida.
valor_max = sum(valores)    # Valor máximo (mochila com todos os objetos).

populacao_inicial = gera_populacao_inicial(tamanho_populacao, n_objetos)

# 3 - AVALIAÇÃO DA APTIDÃO DA POPULAÇÃO INICIAL - - - - - - - - - - - - - - - #

t = 'Espaço de Busca - População Inicial'
valores_mochilas = calcula_valor_populacao(populacao_inicial, valores)
pesos_mochilas = calcula_peso_populacao(populacao_inicial, pesos)
plot_espaco_busca(valores_mochilas, pesos_mochilas, peso_max, t, 1)

t = 'Função Objetivo - População Inicial'
aptidoes = funcao_objetivo(valores_mochilas,pesos_mochilas,valor_max,peso_max)
#plot_funcao_objetivo(valores_mochilas, pesos_mochilas, aptidoes, peso_max, t)

# 4 - CICLO EVOLUTIVO - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

populacao = populacao_inicial
n_geracoes = 26    # Número máximo de gerações (critério de parada).
prob_mutacao = 5    # Probabilidade de ocorrer mutação, em %.
taxa_mutacao = 50    # Quantidade de genes que sofrerão mutação, em %.

for geracao in range(2, n_geracoes):
    
    # 5 - RANKING DE APTIDÃO - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # Geração de uma lista das mochilas que compõe a geração atual, por ordem 
    # de aptidão (da maior para a menor).

    ranking = gera_ranking(aptidoes[:])
    # Printa as 10 melhores mochilas.
    """bests = ranking[0:10]
    for best in bests:
        print(valores_mochilas[best], '---', pesos_mochilas[best])"""
                
    # 6 - SELEÇÃO DOS PAIS - - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # Os pais que se reproduzirão para formar a próxima população serão 
    # selecionados da seguinte forma:
    # 1° + 2° colocados;
    # 2° + 3° colocados;
    # 3° + 4° colocados...

    pais = seleciona_pais(ranking)
    #print('Pais : ')
    #print(pais)
    
    # 7 - CRUZAMENTO - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    
    # O método utilizado será o de 'recombinação com um ponto de corte'.

    nova_populacao = cruzamento(populacao, pais)
    
    # Exibir nova população após cruzamento.
    

    t = 'Espaço de Busca - Geração ' + str(geracao)
    valores_mochilas = calcula_valor_populacao(nova_populacao, valores)
    pesos_mochilas = calcula_peso_populacao(nova_populacao, pesos)
    plot_espaco_busca(valores_mochilas, pesos_mochilas, peso_max, t, geracao)
    
    
    # Delay...
    
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
    


        
