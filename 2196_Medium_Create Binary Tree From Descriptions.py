# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        descriptions = sorted(descriptions)
        all_node = set()  # store all nodes
        leaf_node = set()  # store left nodes
        map_node = defaultdict(list)
        for des in descriptions:
            all_node.add(des[0])
            all_node.add(des[1])

            leaf_node.add(des[1])
            map_node[des[0]].append((des[1], des[2]))

        # find val of root node
        root = (all_node - leaf_node).pop()
        root_node = TreeNode(root)

        def createTree(node):
            """
            node: TreeNode
            """
            if len(map_node[node.val]) == 0:
                return node
            for val, direction in map_node[node.val]:
                if direction == 0:  # right
                    node.right = createTree(TreeNode(val))
                else:  # left
                    node.left = createTree(TreeNode(val))
            return node

        root_node = createTree(root_node)

        return root_node
