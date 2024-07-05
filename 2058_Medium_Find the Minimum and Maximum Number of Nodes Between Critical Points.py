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


# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         # find all critical points and store in a list
#         # process the list
#         store = []
#         current = head
#         while current:
#             store.append(current.val)
#             current = current.next

#         critical = []
#         for i in range(1, len(store) - 1):
#             if (store[i] < store[i - 1] and store[i] < store[i + 1]) or (
#                 store[i] > store[i - 1] and store[i] > store[i + 1]
#             ):
#                 critical.append(i)

#         if len(critical) < 2:
#             return [-1, -1]
#         # print(critical)

#         min_dis = critical[-1] - critical[0]
#         for r in range(1, len(critical)):
#             min_dis = min(min_dis, critical[r] - critical[r - 1])

#         return [min_dis, critical[-1] - critical[0]]
