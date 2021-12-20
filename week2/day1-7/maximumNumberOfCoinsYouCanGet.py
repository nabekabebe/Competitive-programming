class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)
        k = len(piles) // 3
        
        result = 0
        for i in range(len(piles) - k):
            if i % 2 == 1:
                result += piles[i]
        return result
