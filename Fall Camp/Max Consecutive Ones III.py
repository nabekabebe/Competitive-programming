class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        distance = 0

        while right < len(nums):
            if nums[right] == 0 and k > 0:
                k -= 1
                right += 1
            elif nums[right] == 0 and k == 0:
                distance = max(right-left, distance)
                if nums[left] == 0:
                    k += 1

                left += 1
            else:
                right += 1

        distance = max(right-left, distance)

        return distance
