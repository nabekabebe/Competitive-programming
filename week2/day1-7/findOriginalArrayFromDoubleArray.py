class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
                
        if len(changed) == 1 or len(changed) % 2 == 1:
            return []
        
        
        changed.sort()
        
        dic = defaultdict(int)
        for i in changed:
            dic[i] += 1
            
            
        if dic[0] % 2 == 1:
            return []
        
        
        original = []
        
        for i in range(len(changed)):
            val = changed[i]
            val2 = changed[i]*2 
            if dic[val] != 0:
                if val2 in dic:
                    if dic[val2] != 0:
                        original.append(val)
                        dic[val] -= 1

                        dic[val2] -= 1
                    else:
                        return []
                else:
                    return []
        return original
