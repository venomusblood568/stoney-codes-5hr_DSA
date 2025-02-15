# Question Link => https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))
        dic = {}
        for i, num in enumerate(temp):
            if num not in dic:
                dic[num] = i
        
        ret = []
        for i in nums:
            ret.append(dic[i])
        
        return ret