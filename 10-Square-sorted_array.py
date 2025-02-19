# Question Link => https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        ans = [0] * n
        index = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[index] = nums[left] ** 2
                left += 1
            else:
                ans[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return ans