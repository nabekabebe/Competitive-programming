def insertionSort1(n, arr):
    last = arr[n-1]
    for i in range(n-1, -1, -1):
        if i == 0:
            arr[i] = last
        elif arr[i-1] > last:
            arr[i] = arr[i-1]
        else:
            arr[i] = last
            print(*arr)
            break
            
        
        print(*arr)
insertionSort1(10, [2,3,4,5,6,7,8,9,10,1])
