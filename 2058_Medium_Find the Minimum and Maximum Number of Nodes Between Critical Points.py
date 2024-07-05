# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]  # length of linked list <= 3

        prev_node = head
        curr_node = head.next
        next_node = curr_node.next
        pos = 1  # start from index 1
        critical_points = []  # store critical points
        while curr_node:
            if (curr_node.val < prev_node.val and curr_node.val < next_node.val) or (
                curr_node.val > prev_node.val and curr_node.val > next_node.val
            ):
                critical_points.append(pos)
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next
            pos += 1

        if len(critical_points) < 2:
            return [-1, -1]  # length of critical points must be >= 2

        max_distance = critical_points[-1] - critical_points[0]
        min_distance = float("inf")
        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance, critical_points[i] - critical_points[i - 1]
            )

        return [min_distance, max_distance]
