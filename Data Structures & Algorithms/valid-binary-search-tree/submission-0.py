# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubtree(root: Optional[TreeNode], comparator: List[int, int]) -> bool:
            if root is None:
                return True
            if root.val <= comparator[0] or root.val >= comparator[1]:
                return False
            return isValidSubtree(root.left, [comparator[0], root.val]) and isValidSubtree(root.right, [root.val, comparator[1]])

        return isValidSubtree(root, [-1*math.inf, math.inf])