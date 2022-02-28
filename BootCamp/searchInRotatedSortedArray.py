class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, best = 0, len(nums)-1, -1
        
        while left <= right:
            mid  = left +(right-left)//2
            
            
            if nums[mid] == target:
                best = mid
                break
                
            elif nums[left]<=nums[mid]:
                if target >= nums[left] and target<=nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
          
        return best
            
