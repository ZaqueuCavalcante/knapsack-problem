# - - - > Definição das funções utilizadas no decorrer do programa

import random

def calcula_peso_mochila(mochila, pesos):
    # Calcula o peso da mochila passada como parâmetro.

    peso_mochila = 0
    quant_pesos = len(pesos)
    
    for i in range(0, quant_pesos):
        peso_objeto = pesos[i]     # Peso do objeto i.
        zero_ou_um = mochila[i]     # Representa se o objeto i está (1) ou não (0) presente na mochila.
        peso_mochila += zero_ou_um*peso_objeto

    return peso_mochila


def gera_mochila_aleatoria(pesos, peso_max):
    # Função para gerar UM indivíduo/cromossomo/mochila aleatoriamente.
    
    quant_pesos = len(pesos)
    mochila_valida = 0

    while (mochila_valida != 1):    # Enquanto a mochila gerada aleatoriamente não for válida...
        
        mochila_aleatoria = []
        
        for i in range(0, quant_pesos):    # Gera uma mochila aleatória.
            zero_ou_um = random.randint(0, 1)
            mochila_aleatoria.append(zero_ou_um)

        peso_mochila = calcula_peso_mochila(mochila_aleatoria, pesos)
        
        if ( peso_mochila > peso_max):    # Checa se ela é válida (1) ou inválida (0).
            mochila_valida = 0
        else:
            mochila_valida = 1
        
    return mochila_aleatoria


def gera_populacao_inicial(tamanho_populacao, pesos, peso_max):
    # Função para gerar a população inicial de mochilas.
    
    populacao_inicial = []
    quant_pesos = len(pesos)
    
    for i in range(0, tamanho_populacao):
        mochila_aleatoria = gera_mochila_aleatoria(pesos, peso_max)
        populacao_inicial.append(mochila_aleatoria)

    return populacao_inicial


def calcula_valor_mochila(mochila, valores):
    # Calcula a soma dos valores de todos os objetos presentes na mochila.

    valor_mochila = 0
    quant_valores = len(valores)
    
    for i in range(0,quant_valores):
        valor_objeto = valores[i]     # Valor do objeto i.
        zero_ou_um = mochila[i]     # Representa se o objeto i está ou não presente na mochila.
        valor_mochila += zero_ou_um*valor_objeto

    return valor_mochila


def print_lista(lista):
    # Printa os elementos de uma lista quebrando linha a cada elemento.

    for i in lista:
        print(i, '\n')


def funcao_objetivo(pop, valores):
    # Calcula o valor total de cada mochila da população.

    aptidao = []

    for mochila in pop:
        valor_total = calcula_valor_mochila(mochila, valores)
        aptidao.append(valor_total)

    return aptidao

def gera_ranking(aptidao):
    # Gera uma lista dos indivíduos de valores mais altos até os mais baixos.
    # Nela, cada inteiro representa uma mochila.
    # Exemplo: [3,0,1,2]
        # A mochila 3 da população (quarta mochila na lista pop) é a mais aptada.
        # A mochila 0 é a segunda mais apta...

    ranking = []

    for i in range(0, len(aptidao)):
        valor_max = max(aptidao)
        indice = aptidao.index(valor_max)
        ranking.append(indice)
        aptidao[indice] = 0

    return ranking
        




