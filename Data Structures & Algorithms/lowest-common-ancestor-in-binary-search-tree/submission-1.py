# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #base case - return the root if p and q are root.left and root.right
        #if p and q are not children of the root(recursive case)
        
        if p.val<=root.val<q.val or p.val>root.val>=q.val:
            return root
        if p.val==root.val or q.val==root.val:
            return root
        elif (p.val<root.val and q.val<root.val):
            return self.lowestCommonAncestor(root.left, p,q)
            
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p,q)
#dont have to make more methods. Use the trait of the searching trees.
        