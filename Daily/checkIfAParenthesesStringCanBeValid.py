class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) %2 == 1: 
            return False
        
        balanced = 0
        for ch, lock in zip(s, locked):
            if lock == '0' or ch == '(': 
                balanced += 1
            else: 
                balanced -= 1
            if balanced < 0: 
                return False
            
        balanced = 0
        for ch, lock in zip(reversed(s), reversed(locked)): 
            if lock == '0' or ch == ')': 
                balanced += 1
            else: 
                balanced -= 1
            if balanced < 0: 
                return False
            
            
        return True
