class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        
        if (k % 2 == 0):
            return 1 - self.kthGrammar(n, ceil(k/2))
        else:
            return self.kthGrammar(n, ceil(k/2))
        
        
