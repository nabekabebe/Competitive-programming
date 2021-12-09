def countingSort(n, arr):
    lst = [0] * n
    for j in range(n):
        lst[arr[j]] += 1
        
    return lst

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

print(countingSort(n, ar))
