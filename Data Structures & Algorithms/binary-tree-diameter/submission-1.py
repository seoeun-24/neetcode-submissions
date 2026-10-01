# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0

        def counting(node):
            nonlocal max_diameter

            if node is None:
                return 0
            right=counting(node.right)
            left=counting(node.left)

            max_diameter=max(max_diameter,right+left)
            return 1+max(right,left)
        counting(root)
        return max_diameter
        