class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first  = self.binarysearch(nums, target, True)
        answer = [first]
        answer.append(self.binarysearch(nums, target, False))
        
        
        return answer
        
    def binarysearch(self, lst, target, half):
        l = 0
        r = len(lst) - 1
        index = -1
        
        while l <= r:
            
            mid = l + (r-l)//2

            if target > lst[mid]:
                l = mid + 1
                
            elif target == lst[mid]:
                l = l if half else mid + 1
                r = mid-1 if half else r
                index = mid
            
            else:
                r = mid -1
                
            
        return index  
