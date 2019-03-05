def merge_sort(lista): 
    n = len(lista) 
    if(n == 1): return lista 
    izquierda = merge_sort(lista[:int(n/2)]) 
    derecha = merge_sort(lista[int(n/2):]) 
    return merge(izquierda, derecha) 
 
def merge(izquierda, derecha): 
    resultado = [] 
    i = 0 
    j = 0 
    len_izquierda = len(izquierda) 
    len_derecha = len(derecha) 
 
    while(i < len_izquierda or j < len_derecha): 
        if(i >= len_izquierda): 
            resultado.append(derecha[j]) 
            j = j + 1 
        elif(j >= len_derecha): 
            resultado.append(izquierda[i]) 
            i = i + 1 
        elif(izquierda[i] < derecha[j]): 
            resultado.append(izquierda[i]) 
            i = i + 1 
        else: 
            resultado.append(derecha[j]) 
            j = j + 1 
    return resultado 

A = [5,2,3,4,1]
print(merge_sort(A))