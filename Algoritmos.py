from random import *


def quicksort(lista, izq, der):
    i = izq
    j = der
    x = lista[int((izq + der)/2)]

    while(i <= j):
        while lista[i] < x and j <= der:
            i = i+1
        while x < lista[j] and j > izq:
            j = j-1
        if i <= j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            i = i+1
            j = j-1

        if izq < j:
            quicksort(lista, izq, j)
        if i < der:
            quicksort(lista, i, der)

    return lista


def bubbleSort(lista):
    n = len(lista)

    for i in range(1, n):
        for j in range(n-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1

        lista[j] = val

    return lista


def selectionSort(lista):
    n = len(lista)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    medio = int(len(lista) / 2)
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)


def merge(listaA, listaB):
    lista_nueva = []
    a = 0
    b = 0

    while a < len(listaA) and b < len(listaB):

        if listaA[a] < listaB[b]:
            lista_nueva.append(listaA[a])
            a += 1
        else:
            lista_nueva.append(listaB[b])
            b += 1

    while a < len(listaA):
        lista_nueva.append(listaA[a])
        a += 1

    while b < len(listaB):
        lista_nueva.append(listaB[b])
        b += 1

    return lista_nueva


seed()


def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True


def bogo(x):
    while not inorder(x):
        shuffle(x)
    return x


def pesoArbol(arbol):
    if type(arbol) == int:
        return arbol
    elif len(arbol) == 1:
        return pesoArbol(arbol[0])
    else:
        result = 0
        n = len(arbol)
        for i in range(n):
            result += pesoArbol(arbol[i])
        return result


def cantidadElementos(arbol):
    if type(arbol) == int:
        return 1
    elif len(arbol) == 1:
        return cantidadElementos(arbol[0])
    else:
        result = 0
        n = len(arbol)
        for i in range(n):
            result += cantidadElementos(arbol[i])
        return result


def pesoPromArbol(arbol):
    return pesoArbol(arbol)/cantidadElementos(arbol)


def alturaArbol(arbol):
    if type(arbol) == int:
        return 1
    elif len(arbol) == 1:
        return alturaArbol(arbol[0])
    elif len(arbol) == 2 and type(arbol[0]) == int:
        return 1+max(alturaArbol(arbol[0]), alturaArbol(arbol[1]))
    else:
        result = []
        n = len(arbol)
        for i in range(n):
            result.append(alturaArbol(arbol[i]))
        return max(result)
    
def merge_sort2(lista): 
    n = len(lista) 
    if(n == 1): return lista 
    izquierda = merge_sort2(lista[:int(n/2)]) 
    derecha = merge_sort2(lista[int(n/2):]) 
    return merge2(izquierda, derecha) 
 
def merge2(izquierda, derecha): 
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

def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertionSort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result