class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        curr, repeated = set(), set()
        
        for i in range(len(s)-9):
            c = s[i:i+10]
            if c in curr:
                repeated.add(c)
            curr.add(c)
    
        return [*repeated]
    
