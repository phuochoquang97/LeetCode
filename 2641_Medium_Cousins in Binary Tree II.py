# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # find the sum of each level
        level_sum = []
        q = deque()
        current_sum = 0
        q.append(root)
        while q:
            l = len(q)
            for _ in range(l):
                u = q.popleft()
                current_sum += u.val
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
            level_sum.append(current_sum)
            current_sum = 0

        # print(level_sum)

        q.clear()
        current_level = 1
        q.append(root)
        root.val = 0
        while q:
            l = len(q)
            for _ in range(l):
                u = q.popleft()  # u has been replaced
                left_val, right_val = (0, 0)
                if u.left:
                    left_val = u.left.val
                    q.append(u.left)
                if u.right:
                    right_val = u.right.val
                    q.append(u.right)

                if u.left:
                    u.left.val = level_sum[current_level] - left_val - right_val
                if u.right:
                    u.right.val = level_sum[current_level] - left_val - right_val

            current_level += 1

        return root
