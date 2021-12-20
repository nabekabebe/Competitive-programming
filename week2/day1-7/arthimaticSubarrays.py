class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
                
        lst = []
        for i in range(len(l)):
            slst = nums[l[i]:r[i]+1]
            slst.sort()
            dif = slst[1] - slst[0]
            check = True
            for j in range(len(slst)-1):
                if slst[j+1]-slst[j] != dif:
                    check = False
            lst.append(check)
        
        return lst
