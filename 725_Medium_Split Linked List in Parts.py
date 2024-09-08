# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        current = head
        n = 0
        while current:
            n += 1
            current = current.next

        size0 = n // k
        ret_size = [size0] * k
        for i in range(n % k):
            ret_size[i] += 1

        ret = []
        current = head
        part_idx = 0
        count_part_idx = 0
        while current:
            if count_part_idx == 0:
                ret.append(current)
            count_part_idx += 1
            if count_part_idx == ret_size[part_idx]:  # get enough size for part_idx
                temp = current.next
                current.next = None  # create a break point for part_idx linked list
                current = temp

                part_idx += 1
                count_part_idx = 0
                continue

            current = current.next

        if k > n:
            for i in range(n, k):
                ret.append(None)

        return ret
