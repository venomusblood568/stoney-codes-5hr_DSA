# Question link => https://leetcode.com/problems/single-number/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        for i in range(n):
            xor = xor ^ nums[i]

        return xor