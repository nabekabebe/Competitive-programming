class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        
        best = right
        
        while left <= right:
            mid = left +(right -left)//2
            
            result = self.search(nums, mid)
            
            if result[0] < 2 and result[1] < mid:
                left = mid + 1
                
            elif result[0] < 2 and result[1] >= mid:
                right = mid - 1
            else:
                return mid

    
    def search(self, nums, val):
        count, index, before = 0, -1, 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                index = i
               
            elif nums[i] < val:
                before += 1
        return (count, before)
    
