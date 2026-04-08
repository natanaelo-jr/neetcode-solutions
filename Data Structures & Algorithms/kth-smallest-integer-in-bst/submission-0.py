# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # while list.len < k
        # dfs_left
        # insert node
        # dfs_right
        def dfs(node, node_list):
            if len(node_list) >= k:
                return
            if node.left:
                dfs(node.left, node_list)
            node_list.append(node)
            if node.right:
                dfs(node.right, node_list)


        node_list = []
        if root:
            dfs(root, node_list)
        return node_list[k-1].val