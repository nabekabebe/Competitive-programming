class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        # nums.sort()
        
        nums.sort(key=lambda x: (int((str(x) + str(((9-len(str(x)))*str(x))))[:9]), len(str(x))), reverse=True)
        
        result  = ""
        for i in nums:
            result += str(i)
        
        return "0" if (result[0] == "0") else result
    
