# Question Link -> https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return root
        
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
            