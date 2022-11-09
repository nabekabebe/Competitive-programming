class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)

        for k, v in count.items():
            if v > 1:
                ans.append(k)

        for i in range(1, len(nums)+1):
            if i not in count:
                ans.append(i)

        return ans
