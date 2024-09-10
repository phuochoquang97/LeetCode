# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        current = head.next

        def GCD(a, b):
            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a

            return a

        while current:
            # todo: insert here
            current_val = current.val
            prev_val = prev.val

            temp = ListNode(GCD(current_val, prev_val))

            prev.next = temp
            temp.next = current
            prev = current
            current = current.next

        return head
