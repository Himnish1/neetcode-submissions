# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # because this is a bst, we can use integer comparisons to traverse
        # 
        current_node = root

        while current_node is not None:
            comparator = current_node.val
            if p.val < comparator and q.val > comparator:
                # split
                return current_node
            if p.val > comparator and q.val < comparator:
                # split
                return current_node
            
            if p.val == comparator:
                # likely lowest decendant
                return p
            elif q.val == comparator:
                return q

            if p.val < comparator:
                # go to left subtree
                current_node = current_node.left
            elif p.val > comparator:
                # go to right subtree
                current_node = current_node.right
            


        

