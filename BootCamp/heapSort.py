#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def downHeapify(self,arr, n, i):
        # code here
        left = self.getLeftChild(arr, n, i)
        right = self.getRightChild(arr, n, i)
        
        if left >= 0 and right >= 0: 
            if arr[left] > arr[right]:
                if arr[i] > arr[right]:
                    arr[right], arr[i] = arr[i], arr[right]
                    return self.downHeapify(arr, n, right)
            else:                
                 if arr[i] > arr[left]:
                    arr[left], arr[i] = arr[i], arr[left]
                    return self.downHeapify(arr, n, left) 
        elif left >= 0:
            if arr[i] > arr[left]:
                arr[left], arr[i] = arr[i], arr[left]
                return self.downHeapify(arr, n, left)   


    def upHeapify(self,arr, n, i):
        # code here
        parent = self.getParent(i)
        if parent >= 0:
            if arr[parent] > arr[i]:
                arr[i], arr[parent] = arr[parent], arr[i]
                return self.upHeapify(arr, parent)
                
                
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1, -1, -1):
            self.downHeapify(arr, n, i)
        
    def insert(self, arr, n, value):
        arr.append(value)
        self.upHeapify(arr, n, len(arr)-1)
        self.downHeapify(arr, n, len(arr) -1)

        
    def remove(self, arr, n, index):
        arr[index], arr[n-1] = arr[n-1], arr[index]
        self.upHeapify(arr, n-1, index)

        self.downHeapify(arr, n-1, index)

    def update(arr, index, n, value):
        arr[index] =  value
        self.upHeapify(arr, n, index)
        self.downHepify(arr, n, index)
 
  
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(n):
            self.remove(arr, n-i, 0)
            
        arr.reverse()    
            

    def getLeftChild(self, arr, n, index):
        if n > 2*index+ 1:
            return 2*index + 1
        return -1
        
    def getRightChild(self, arr, n, index):
        if n > 2*index + 2:
            return 2*index + 2
        return -1 
        
    def getParent(self, index):
        if index > (index-1)//2:
            return (index-1)//2
        return -1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
