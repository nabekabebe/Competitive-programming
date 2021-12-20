class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        
        size = len(nums)
        left = 0
        right = 0
        
        max_count = 0
        while right < size:
            result  = right-left+1
            max_count = max(max_count, result)    
            dif = nums[left] - nums[right]

            if dif <= k:
                right += 1
                k -= dif  
            else:
                left += 1
                k +=  (right - left)*(nums[left-1]-nums[left]) 

            
        return max_count
                   
