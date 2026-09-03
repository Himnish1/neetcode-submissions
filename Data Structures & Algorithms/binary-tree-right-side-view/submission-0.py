# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # sounds like depth first search starting on the right
        # 1, push left, push right 
        processing_queue = deque()
        return_list = []
        processing_queue.append(root)

        while len(processing_queue) != 0:
            qLen = len(processing_queue)
            rightmost = None
            for i in range(qLen):
                current = processing_queue.popleft()
                if current is None:
                    continue
                rightmost = current
                processing_queue.append(rightmost.left)
                processing_queue.append(rightmost.right)
            if rightmost is not None:
                return_list.append(rightmost.val)
        return return_list