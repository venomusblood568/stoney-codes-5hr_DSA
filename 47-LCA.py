# Question Link -> https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        l = lowestCommonAncestor(root.left,p,q)
        r = lowestCommonAncestor(root.right,p,q)

        if l and r:
            return root
        return l or r

