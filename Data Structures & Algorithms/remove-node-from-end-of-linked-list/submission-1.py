# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead_pointer = head
        after_pointer = head

        # Caminha com r n vezes
        for i in range(n):
            if not after_pointer:
                return head
            after_pointer = after_pointer.next

        # Se r for o fim da lista, o que sai é o head
        if after_pointer is None:
            head = head.next
            return head

        # Caminha com l e r até r ser o fim
        while after_pointer.next is not None:
            ahead_pointer = ahead_pointer.next
            after_pointer = after_pointer.next
        

        aux = ahead_pointer.next
        if aux:
            ahead_pointer.next = ahead_pointer.next.next
            aux.next = None
            
        return head