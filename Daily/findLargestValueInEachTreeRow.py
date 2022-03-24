# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])
        while queue:
            maxx = -float('inf')
            nxt = deque([])
            while queue:
                top = queue.popleft()
                maxx = max(maxx, top.val)
    
                if top.left:
                    nxt.append(top.left)
                if top.right:
                    nxt.append(top.right)
            ans.append(maxx)
            queue = nxt
        
        return ans
