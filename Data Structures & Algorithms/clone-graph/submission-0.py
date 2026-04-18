"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = dict()
        def createNodes(reference):
            if reference is None:
                return None
            newNode = Node(reference.val)
            newNeighbors = []
            created[newNode.val] = newNode
            for neighbor in reference.neighbors:
                key = neighbor.val
                if created.get(key, False):
                    newNeighbors.append(created[neighbor.val])
                else:
                    newNeighbors.append(createNodes(neighbor))
            newNode.neighbors = newNeighbors
            return newNode
        return createNodes(node)