class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left , right, n, best = 0, len(citations)-1, len(citations) - 1, 0
        
        while left <= right:
            mid = left + (right -left)//2
            
            if citations[mid] <= n - mid:
                left = mid + 1
            else:
                right = mid - 1
                best =  max(n - mid + 1, best)
        
        
        return best 
