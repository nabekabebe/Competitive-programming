class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars, answer = Counter(s), 0
        for tc in chars:
            flipsInWindow, l = 0, 0   
            for r, rc in enumerate(s):
                if rc != tc:
                    flipsInWindow += 1
                    
                while flipsInWindow > k:
                    if s[l] != tc:
                        flipsInWindow -= 1
                    l += 1
        
                answer = max(answer, r - l + 1)
        return answer
