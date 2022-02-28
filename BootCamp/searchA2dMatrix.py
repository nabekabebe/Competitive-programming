class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right, result  = 0, len(matrix) - 1, False
        
        
        while left <= right:
            mid  = left + (right-left)//2
            
            if matrix[mid][0] > target:
                right = mid - 1

            else:
                result = self.find(matrix[mid], target)
                left = mid + 1
                
        return result
                
    def find(self, arr, target): 

        left, right = 0, len(arr) - 1
        while left <= right:
            mid  = left + (right-left)//2
            
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                return True
        return False
