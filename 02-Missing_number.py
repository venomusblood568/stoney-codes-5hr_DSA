# Question Link => https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = n*(n+1)//2
        sum_arr = 0
        for i in range(n):
            sum_arr += nums[i]
        
        missing_num = sum_n - sum_arr
        return missing_num