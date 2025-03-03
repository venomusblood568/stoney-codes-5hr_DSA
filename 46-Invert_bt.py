# Question Link -> https://leetcode.com/problems/invert-binary-tree/

class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left , root.right = root.right ,root.left
        return root