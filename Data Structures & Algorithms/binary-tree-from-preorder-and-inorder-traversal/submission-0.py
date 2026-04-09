# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = list() # 1 2
        root = TreeNode(preorder[0])
        last_inserted = root # 2
        to_right_node = None
        stack.append(root)
        inorder_pointer = 0 # 0
        preorder_pointer = 1 # 1
        # 4
        # 3 4
        while preorder_pointer < len(preorder):
            while len(stack) > 0 and inorder[inorder_pointer] == stack[-1].val:
                to_right_node = stack.pop() # 1
                inorder_pointer+=1 # 2

            val = preorder[preorder_pointer] # 3
            new_node = TreeNode(val) # 3
            stack.append(new_node) # 3
            preorder_pointer += 1 # 3

            if to_right_node is not None:
                to_right_node.right = new_node
                to_right_node = None
            else:
                last_inserted.left = new_node
            last_inserted = new_node

        return root