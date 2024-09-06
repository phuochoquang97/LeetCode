# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        current = head
        prev = head

        while current:
            if current.val in nums:  # current.val in nums
                if current == head:  # current is head, set head = current.next
                    head = current.next
                else:  # delete current
                    prev.next = current.next
            else:  # current.val not in nums
                prev = current

            current = current.next

        return head
