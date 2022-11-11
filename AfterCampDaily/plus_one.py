class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            num = digits[i] + carry
            digits[i] = num % 10
            carry = num // 10

        if carry:
            digits = [carry] + digits

        return digits
