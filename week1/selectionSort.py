def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        for j in range(i+1, n):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        
    return arr



