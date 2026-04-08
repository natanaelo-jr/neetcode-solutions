# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, minimum, maximum, node: TreeNode) -> bool:
        if node.val <= minimum or node.val >= maximum:
            return False
        left = True
        right = True
        if node.left:
            left = self.search(minimum, node.val, node.left)
        if node.right:
            right = self.search(node.val, maximum, node.right)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.search(-1001, 1001, root)
        