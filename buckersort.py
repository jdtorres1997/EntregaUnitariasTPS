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

A = [1]
print(bucket_sort(A))