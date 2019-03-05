
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
    comparaciones = 0

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
            comparaciones += 1

        lista[j] = val

    return lista

def shellSort(lista):
    comparaciones = 0
    n = len(lista)
    gap = int (n / 2)

    while gap > 0:
        for i in range(gap, n):
            val = lista[i]
            j = i
            comparaciones += 1

            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val

        gap = int (gap / 2)
    return lista

def selectionSort(lista):
    comparaciones = 0
    n = len(lista)

    for i in range(n - 1):
        menor = i
        comparaciones += 1

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    medio =int (len(lista) / 2)
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)

def merge(listaA, listaB):
    comparaciones = 0
    lista_nueva = []
    a = 0
    b = 0

    while a < len(listaA) and b < len(listaB):
        comparaciones += 1

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