def targetIndices(nums, target: int):
    # using BubbleSort
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] =   nums[j], nums[j+1]    
    output = []
    for i in range(len(nums)):
        if target == nums[i]:
            output.append(i)  
    return output

print(targetIndices([12,3,4,5,6,7,4], 4))
            
   
