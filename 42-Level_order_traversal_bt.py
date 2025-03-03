# Question Link -> https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = [root]

        while q:
            level_size = len(q)
            level = []
            for i in range(level_size):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans