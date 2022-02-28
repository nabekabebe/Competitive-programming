class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        divisor = right
        
        while left <= right:
            mid = left +(right -left)//2
            
            summ = sum([math.ceil(i/mid) for i in nums])
                        
            if summ <= threshold:
                right = mid - 1
                divisor = mid
            
            else:
                left = mid + 1
                
                
        return divisor
