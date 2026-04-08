# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        turtle = head.next
        if not turtle:
            return False
        rabbit = turtle.next
        if not rabbit:
            return False

        while turtle and rabbit:
            if turtle == rabbit:
                return True
            if turtle.next and rabbit.next:
                turtle = turtle.next
                rabbit = rabbit.next.next
            else:
                return False
        return False
        