# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(node: TreeNode) -> List:
            if not node:
                return defaultdict(int)

            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            left_dis = dfs(node.left)
            right_dis = dfs(node.right)

            for ld in left_dis:
                for rd in right_dis:
                    if ld + rd <= distance:
                        self.pairs += left_dis[ld] * right_dis[rd]

            all_dis = defaultdict(int)
            for ld in left_dis:
                if ld + 1 <= distance:
                    all_dis[ld + 1] += left_dis[ld]

            for rd in right_dis:
                if rd + 1 <= distance:
                    all_dis[rd + 1] += right_dis[rd]

            return all_dis

        dfs(root)

        return self.pairs
