class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        size = len(nums)
        
        for i in range(size):
            col = nums[i]
            nums[i] = 2
            
            if col < 2:
                nums[white] = 1
                white += 1
            if col == 0:
                nums[red] = 0
                red += 1
                
        
                
        return nums
