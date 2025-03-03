# Question Link -> https://leetcode.com/problems/average-of-levels-in-binary-tree/

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if not root:
            return ans

        q = [root]
        while q:
            n = len(q)
            s = 0
            
            for i in range(n):
                node = q.pop(0)
                s += node.val

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            ans.append(s/n)
        
        return ans