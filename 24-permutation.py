# Question Link => https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,path):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                backtrack(nums[:] + nums[i+1:],path+ nums[i])

        result = []
        backtrack(nums,[])
        return result