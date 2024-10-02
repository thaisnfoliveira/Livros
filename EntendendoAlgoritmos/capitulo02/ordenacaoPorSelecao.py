def menor(array):
    menor = array[0]
    menor_indice = 0

    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    
    return menor_indice

def ordenacaoPorSelecao(array):
    novoArray = []
    for i in range(1, len(array)):
        menor = menor(array)
        novoArray.append(array.pop(menor))
    return novoArray