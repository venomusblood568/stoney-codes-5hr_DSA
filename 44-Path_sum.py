# Question Link -> https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        leftSum = self.hasPathSum(root.left, targetSum - root.val)
        rightSum = self.hasPathSum(root.right, targetSum - root.val)

        return leftSum or rightSum