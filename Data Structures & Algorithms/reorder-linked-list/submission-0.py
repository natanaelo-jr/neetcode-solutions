# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        aux = head
        while aux is not None:
            stack.append(aux)
            aux = aux.next


        left = head
        right = stack.pop()
        while left is not right and left.next is not right:
            
            aux = left.next
            left.next = right
            right.next = aux

            left = aux
            right = stack.pop()
            
        if right is not None:
            right.next = None
        # 1 -> 2 -> 3
        # 1 -> 3 <-> 2

        # 1 -> 2 -> 3 -> 4
        # 1 -> 4 -> 2 -> 3 -> 4 
