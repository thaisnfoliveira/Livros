def somaRecursiva(array):

    if len(array) == 0:
        return
    
    else:
        return array[0] + somaRecursiva(array[1:])
    

minha_lista = [0, 1, 2, 3]
print(somaRecursiva(minha_lista))