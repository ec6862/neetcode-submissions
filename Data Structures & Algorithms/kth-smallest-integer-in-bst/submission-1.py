# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        k_value = 0

        def dfs(node):
            nonlocal count, k_value
            if not node:
                return

            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                k_value = node.val
            dfs(node.right)

            return

        dfs(root)

        return k_value
            