class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)
        best = right
        
        while left <= right:
            mid  = left + (right -left)//2
            if self.summation(weights, mid) > days:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
            
            
        return best
    
    
    def summation(self, arr, val):
        result = 0
        
        day = 1
        for i in arr:
            if result + i <= val:
                result += i
            else:
                day += 1
                
                result = i
                
        return day
