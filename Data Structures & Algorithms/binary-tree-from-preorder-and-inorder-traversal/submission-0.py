# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we are given
            # preorder: root --> left --> right
            # inorder: left --> root --> right
        
        # preorder gives us the root as the first index
        # inorder tells us what is on the left side and right side
        # combining these two information
            # we know the root
            # we know what is on the left, and what is on the right
        hashMap = {}
        for index, num in enumerate(inorder):
            hashMap[num] = index
        globalIndex = 0

        def dfs(l, r):
            nonlocal globalIndex
            if l > r:
                return None
            
            root_val = preorder[globalIndex]
            globalIndex += 1
            root = TreeNode(root_val)
            mid = hashMap[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)
            
            