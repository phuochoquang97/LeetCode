# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # head of returned linked list
        current_node = head.next  # ignore the first zero value
        node = dummy
        while current_node:
            current_sum = 0
            while current_node and current_node.val != 0:
                # calculathe the sum of all node in range 0 - 0
                current_sum += current_node.val
                current_node = current_node.next

            if current_sum != 0:
                # create a new node in returned linked list
                node.next = ListNode(current_sum)
                node = node.next
            if current_node:
                # skip zero-value node
                current_node = current_node.next

        return dummy.next
