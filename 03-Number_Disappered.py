# Question Link => https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        ret = []
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                ret.append(i)
        return ret 