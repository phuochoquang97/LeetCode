# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0

        def dfs(node: TreeNode):
            if not node:  # node is None
                return

            dfs(node.right)
            self.val += node.val  # keep track of total sum of node whoes val is greater than val of current node
            node.val = self.val
            dfs(node.left)

        dfs(root)

        return root
