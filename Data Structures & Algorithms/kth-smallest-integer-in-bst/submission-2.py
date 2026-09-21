# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        i_count = 0

        def dfs(node):
            nonlocal count, i_count

            if not node:
                return None
            
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                i_count = node.val
            dfs(node.right)
        
        dfs(root)

        return i_count
