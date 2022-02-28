class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in grid:
            left, right, n, index = 0, len(i)-1, len(i), -1
            
            while left <= right:
                mid = left + (right -left) // 2
                
                if i[mid] >= 0:
                    left = mid + 1
                
                else:
                    right = mid - 1 
                    index = mid
                    
            count += n - index if index >= 0 else 0
                    
          
                    
        return count
