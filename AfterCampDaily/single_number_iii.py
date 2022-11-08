class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val = 0
        for num in nums:
            val ^= num

        bit = 1
        while (val & 1) == 0:
            val = val >> 1
            bit = bit << 1

        num1, num2 = 0, 0
        for num in nums:
            if (bit & num) != 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
