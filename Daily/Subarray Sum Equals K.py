class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summ, val = 0, 0, {0:1}
        
        for i in nums:
            summ += i
            if summ - k in val:
                count += val[summ-k]

            if summ not in val:
                val[summ] = 1
            else:
                val[summ] += 1

        return count
