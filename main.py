import funcoes

# 1 - REPRESENTAÇÃO DE CADA INDIVÍDUO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# Lista de objetos que podem ser adicionados à mochila, cada qual com determinado valor e peso.
# Cada tupla (valor, peso) representa um objeto.

objetos = [(10,0.5), (50,1.5), (60,2), (1500,3), (1,2.3), (600,0.2), (5,1.1), (6,2.5), (150,0.3), (80,2), (1,0.02)]
quant_objetos = len(objetos)
valores = []
pesos = []

for i in range(0, quant_objetos):
    valores.append(objetos[i][0])    # Lista com os 'valores' de todos os objetos.
    pesos.append(objetos[i][1])    # Lista com os 'pesos' de todos os objetos.

# Cada indivíduo será representado através de uma lista, na qual:
    # 0 -> indica que o objeto não está presente na mochila.
    # 1 -> indica que o objeto está presente na mochila.
    # Exemplo de mochila:
        # m = [1,0,0,0,0,0,0,0,0,1,0] -> apenas o primeiro e o penúltimo objeto está presente na mochila.

# 2 - GERAÇÃO DA POPULAÇÃO INICIAL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

tamanho_populacao = 5    # Tamanho da população.

peso_max = 10    # Capacidade máxima de carga, igual para todas as mochilas geradas.

pop = funcoes.gera_populacao_inicial(tamanho_populacao, pesos, peso_max)    # Lista com a população inicial gerada.

print('\n- - - > População inicial: \n')
funcoes.print_lista(pop)

# 3 - AVALIAÇÃO DA POPULAÇÃO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Feita através de uma função objetivo, que avalia a aptidão do indivíduo (mochila) como solução do problema.

aptidao = funcoes.funcao_objetivo(pop, valores)

print('\n- - - > Valores totais de cada mochila: \n')
funcoes.print_lista(aptidao)

# As mochilas avaliadas são colocadas em um ranking de valores totais.

ranking = funcoes.gera_ranking(aptidao)

print('\n- - - > Ranking: \n')
funcoes.print_lista(ranking)




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# SELEÇÃO DOS MELHORES INDIVÍDUOS

def gera_ranking(pop, valores):
    # Função que retorna uma lista com as melhores mochilas (maior valor total).

    tam_pop = len(pop)
    






        
