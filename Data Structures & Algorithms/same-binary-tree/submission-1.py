# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def sameTree(firstTree, secondTree):
            if not firstTree and not secondTree:
                return True
            if firstTree and not secondTree or not firstTree and secondTree:
                return False
            if firstTree.val != secondTree.val:
                return False
            
            left = sameTree(firstTree.left, secondTree.left)
            right = sameTree(firstTree.right, secondTree.right)
            
            return left and right

        return sameTree(p, q)
