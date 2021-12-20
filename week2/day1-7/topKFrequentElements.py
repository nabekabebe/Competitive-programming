class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)
        for i in nums:
            values[i] += 1
            
        result = []
        for i in range(k):
            fin_max = max(values, key=values.get)
            result.append(fin_max)
            
            values[fin_max] = 0
                    
        return result
