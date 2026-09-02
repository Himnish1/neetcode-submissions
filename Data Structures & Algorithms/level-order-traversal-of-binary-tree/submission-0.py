# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1, 2, 3, 4, 5, 6, 7
        # processing_queue = 1
        # while processing queue, pop children and add them to processing queue
        return_list = []

        if root is None:
            return return_list

        processing_queue = deque()
        processing_queue.append(root)

        while len(processing_queue) != 0:
            # pop all things in processing queue to populate next level
            next_level = []
            current_level = []
            while len(processing_queue) != 0:
                current_node = processing_queue.popleft()
                if current_node is None:
                    continue
                next_level.append(current_node.left)
                next_level.append(current_node.right)
                current_level.append(current_node.val)
            if current_level != []:
                return_list.append(current_level)
            processing_queue.extend(next_level)
        return return_list