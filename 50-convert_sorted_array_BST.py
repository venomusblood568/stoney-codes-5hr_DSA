# Question Link -> https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class Solution(object):
    def sortedArrayToBST(self, nums):
        def recursive(start,end):
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = recursive(nums,0,mid-1)
            node.right =  recursive(nums,mid+1,end)
            return node

        return recursive(nums,0,len(nums)-1)