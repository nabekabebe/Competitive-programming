def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] =   a[j], a[j+1]
                count +=1
        
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
       

