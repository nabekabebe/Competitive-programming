class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                ans[i] = ans[i-1] * nums[i-1]

        after = nums[len(nums) - 1]
        for i in range(len(nums) - 1, 0, -1):
            ans[i-1] = ans[i-1] * after
            after *= nums[i-1]

        return ans
