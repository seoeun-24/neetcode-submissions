# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def finding(node):
            nonlocal res
            if node is None:
                return 
            answer = finding(node.left)
            if answer is not None:
                return answer
            res += 1
            if res == k:
                return node.val
            answer = finding(node.right)
            if answer is not None:
                return answer

        return finding(root)