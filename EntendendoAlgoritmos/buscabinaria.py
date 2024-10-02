def busca_binaria(array, elem):
    left_index = 0;
    right_index = len(array) - 1;

    result = None

    while left_index <= right_index:
        item_meio = (left_index + right_index)/2 #essa variável sera arredondada automaticamente para baixo se o resultado não for par
        chute = array[item_meio]

        if chute == elem:
            result = item_meio
        elif chute > elem:
            right_index = item_meio -1
        else:
            left_index = item_meio + 1
        
    return result

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(busca_binaria(array, 2)) #resultado esperado: 1
print(busca_binaria(array, 11)) #resultado esperado: None