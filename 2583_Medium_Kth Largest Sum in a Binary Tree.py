# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # bfs
        list_sum = []
        current_level = 1
        current_sum = 0

        q_current = deque()
        q_next = deque()
        q_current.append(root)

        while q_current:
            u = q_current.pop()
            current_sum += u.val

            if u.left:
                q_next.append(u.left)

            if u.right:
                q_next.append(u.right)

            if not q_current:  # iterate all nodes in current level
                list_sum.append(current_sum)
                current_level += 1
                current_sum = 0
                q_current = q_next.copy()
                q_next.clear()

        list_sum = sorted(list_sum, reverse=True)

        return -1 if k > len(list_sum) else list_sum[k - 1]
