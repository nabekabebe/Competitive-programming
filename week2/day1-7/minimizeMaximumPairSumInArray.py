class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        maximum = 0
        for i in range(len(nums)//2):
            minimum = nums[i] + nums[-1+(i*-1)]
            if minimum > maximum:
                maximum = minimum
        
        return maximum
                
        
