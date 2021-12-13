class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(1, len(nums)-1):
            if i % 2 == 1:
                nums[i+1], nums[i] = nums[i], nums[i+1]

        return nums
