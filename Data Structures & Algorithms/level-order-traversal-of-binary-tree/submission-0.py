# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        root_info = (root, 0)
        if root:
            queue.append(root_info)
        levels = list()

        while len(queue) > 0:
            front = queue.popleft()
            level = front[1]
            if len(levels) == level:
                levels.append([front[0].val])
            else:
                levels[level].append(front[0].val)

            if front[0].left:
                queue.append((front[0].left, level+1))
            if front[0].right:
                queue.append((front[0].right, level+1))
        
        return levels