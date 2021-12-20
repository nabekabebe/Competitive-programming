class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count = 0
        lst = defaultdict(int)
        for i in nums:
            lst[i] += 1
   
        for i in range(len(nums)):
            pt1 = lst[nums[i]]
            if pt1 > 0:
                lst[nums[i]] -= 1
                pt2 = lst[k-nums[i]]
                if pt2 > 0:
                    lst[k-nums[i]] -= 1
                    count += 1
            
        return count
            
