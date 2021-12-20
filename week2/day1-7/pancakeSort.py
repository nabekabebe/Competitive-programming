class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        result = []
        for i in range(len(arr)):
            end = len(arr) - i
            index = self.get_max_index(arr, end)
            
            array = arr[:index+1][::-1] + arr[index+1:end]
            new_array = array[::-1]
            
            last_array = new_array + arr[end: len(arr)]
            
            result.append(index+1)
            result.append(end)
            
            arr = last_array
        return result
    
    
    def get_max_index(self,nums, last):
        for i in range(last+1):
            if nums[i] == last:
                return i
            
    
    
            
