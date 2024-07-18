# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_del = set(to_delete)
        ret = []

        def trace(node: TreeNode, is_root: bool) -> TreeNode:
            if not node:
                return None
            is_deleted = node.val in to_del
            if is_root and not is_deleted:  # add root of tree to result
                ret.append(node)

            # if parent is deleted, children are roots of new trees
            node.left = trace(node.left, is_deleted)
            node.right = trace(node.right, is_deleted)

            # assign None to root if deleted
            return node if not is_deleted else None

        root = trace(root, True)

        return ret
