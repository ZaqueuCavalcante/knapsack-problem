from random import randint

def gera_mochila_aleatoria(n_objetos):
    # Gera UM indivíduo/cromossomo/mochila aleatoriamente.
        
    mochila_aleatoria = []
        
    for i in range(0, n_objetos):
        zero_ou_um = randint(0, 1)
        mochila_aleatoria.append(zero_ou_um)
        
    return mochila_aleatoria