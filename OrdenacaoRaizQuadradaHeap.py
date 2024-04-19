import math
import random
import time

def heapify(arr, i, tamanho):
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i
    
    if esquerda < tamanho and arr[esquerda] > arr[maior]:
        maior = esquerda
    
    if direita < tamanho and arr[direita] > arr[maior]:
        maior = direita
    
    if i != maior:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, maior, tamanho)

def make_heap(arr):
    tamanho = len(arr)
    for i in range(tamanho // 2 - 1, -1, -1):
        heapify(arr, i, tamanho)

def remove_heap(arr):
    if len(arr) == 1:
        return arr.pop()
    maior = arr[0]
    arr[0] = arr.pop()
    make_heap(arr)
    return maior

def ordenacao(arr):
    listaFinal = []
    heapAux = []

    tamanho = len(arr)
    tamanhoSub = int(math.sqrt(tamanho))
    subHeaps = []
    for i in range(0,tamanho, tamanhoSub):
        subHeap = arr[i:i+tamanhoSub]
        subHeaps.append(subHeap)
    
    for subHeap in subHeaps:
        make_heap(subHeap)
    
    for subHeap in subHeaps:
        heapAux.append(remove_heap(subHeap))
    make_heap(heapAux)

    indice = 0
    for i in range(0,tamanho):
        n = len(subHeaps)
        listaFinal.insert(0, remove_heap(heapAux))
        for j in range(0, n):
            if not subHeaps[j]:
                subHeaps.pop(j)
                n = len(subHeaps)
                break
        if indice >= n:
            indice = n - 1
        if len(subHeaps) > 1:
            make_heap(subHeaps[indice])
        for j in range(0,n):
            if subHeaps[j][0] > subHeaps[indice][0]:
                indice = j
        if len(subHeaps) > 0:
            heapAux.append(remove_heap(subHeaps[indice]))
            make_heap(heapAux)

    #print(listaFinal) 


tamanho = 10**7
v = random.sample(range(0, tamanho), tamanho)
make_heap(v)
inicioTempo = time.time()
ordenacao(v)
fimTempo = time.time()
mediaTempo = fimTempo - inicioTempo
print(mediaTempo)
