class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        
        
        count = {}
        for i in range(len(nums1)):
            count[nums1[i]] = i
        
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                temp = stack.pop()
                if temp in count:
                    result[count[temp]] = num
            stack.append(num)
            
        return result
