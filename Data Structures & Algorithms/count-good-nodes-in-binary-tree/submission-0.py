# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(root: TreeNode, max_val: int) -> int:
            if root is None:
                return 0

            if root.val >= max_val:
                return 1 + countGoodNodes(root.left, root.val) + countGoodNodes(root.right, root.val)
            
            else:
                return 0 + countGoodNodes(root.left, max_val) + countGoodNodes(root.right, max_val)
        
        return countGoodNodes(root, -1*math.inf)