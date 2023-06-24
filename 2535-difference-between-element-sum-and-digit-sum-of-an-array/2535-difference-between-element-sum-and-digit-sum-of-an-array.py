class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_of_elements = 0
        sum_of_digits = 0
        for num in nums:
            sum_of_elements += num
            while num > 0:
                sum_of_digits += num % 10
                num = num // 10
        return abs(sum_of_elements - sum_of_digits)