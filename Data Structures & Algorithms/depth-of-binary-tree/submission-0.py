# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque()
        node_info = (1, root)        
        queue.append(node_info)
        max_depth = 0
        while len(queue) > 0:
            current = queue.popleft()
            node = current[1]
            level = current[0]
            max_depth = max(max_depth, level)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))

        return max_depth