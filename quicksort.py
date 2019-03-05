def quicksort(lista, izq, der):
    i = izq
    j = der
    x = lista[int((izq + der)/2)]

    while(i <= j):
        while lista[i] < x and j <= der:
            print("While 1", lista)
            i = i+1
        while x < lista[j] and j > izq:
            print("While 2", lista)
            j = j-1
        if i <= j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            i = i+1
            j = j-1
            print("IF 1", lista)

        if izq < j:
            print("IF 2", lista)
            quicksort(lista, izq, j)
        if i < der:
            print("IF 3", lista)
            quicksort(lista, i, der)
    
    return lista


def imprimeLista(lista, tam):
    for i in range(0, tam):
        print(lista[i])


def leeLista():
    lista = []
    cn = int(input("Cantidad de numeros a ingresar: "))

    for i in range(1, cn+1):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista

'''
A = leeLista()
resultado = quicksort(A, 0, len(A)-1)
imprimeLista(resultado, len(resultado))
'''
A = [1,2,3,4,5]
resultado = quicksort(A, 0, 4)
imprimeLista(resultado, len(resultado))