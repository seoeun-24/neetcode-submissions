# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checking(node,minval,maxval):
            if node is None:
                return True

            if not (minval < node.val < maxval):
                return False

            left = checking(node.left, minval, node.val)
            right = checking(node.right, node.val, maxval)

            return left and right
        return checking(root, float('-inf'), float('inf'))

            