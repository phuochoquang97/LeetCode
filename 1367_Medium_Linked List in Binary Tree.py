# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # Helper function to check if there is a matching path starting from the current tree node
        def dfs(node, current):
            if not current:  # We've matched the entire linked list
                return True
            if not node:  # Reached a leaf in the tree and haven't matched the list
                return False
            if node.val == current.val:  # Values match, try to continue along the path
                return dfs(node.left, current.next) or dfs(node.right, current.next)
            return False  # Values don't match, stop exploring this path

        # Main function to traverse the tree and look for potential matches
        def traverse(node):
            if not node:
                return False
            # Try starting a path from the current node or explore left/right subtrees
            return dfs(node, head) or traverse(node.left) or traverse(node.right)

        return traverse(root)
