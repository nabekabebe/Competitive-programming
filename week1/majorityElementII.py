class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        lst = []

        if len(nums) == 1:
            return nums
        
        a = [nums[0], 1]
        count = 1
        for i in range(1, len(nums)):
            if a[0] == nums[i]:
                count +=1
                a = [a[0], count]
                
                if i == (len(nums)-1):
                    lst.append(a)
            else: 
                if i == (len(nums)-1):
                    lst.append([nums[i], 1])
                lst.append(a)
                a = [nums[i], 1]
                count = 1
    
        return [num[0] for num in lst if num[1] > (len(nums) / 3)]
