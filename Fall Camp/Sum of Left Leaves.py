# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l):
            if not node:
                return 0

            left = dfs(node.left, True)
            right = dfs(node.right, False)

            if not node.left and not node.right and l:
                return node.val

            return left + right

        return dfs(root, False)
