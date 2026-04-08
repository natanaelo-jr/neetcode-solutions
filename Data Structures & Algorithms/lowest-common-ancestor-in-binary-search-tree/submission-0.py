# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # se current > p && > q: left
        # se current < p && < q: right
        # se current <= p && >= q: ele eh o ancestral comum
        # Generalizando: Se vou pra lados diferentes da árvora ou se meu 
        # nó é um dos dois que busco, automaticamente retorno ele

        node = root
        while node:
            if node.val == p.val or node.val == q.val:
                return node
            if node.val > p.val:
                if node.val > q.val:
                    node = node.left
                else:
                    return node

            elif node.val < p.val:
                if node.val < q.val:
                    node = node.right
                else:
                    return node

        return None